"""
Agent Loop - 智能体循环模块
A minimal agent loop that extracts knowledge triples from text.

This demonstrates the core Agent Loop pattern:
  Perceive (感知) → Think (思考) → Act (行动) → Observe (观察)

The loop retries if extraction confidence is low (max 3 iterations).
"""

import json
import os
from openai import OpenAI

from app.graph_store import graph_store

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))

EXTRACTION_PROMPT = """Extract knowledge triples (subject, relation, object) from the following text.
Return a JSON object with:
- "triples": list of {"subject": str, "relation": str, "object": str}
- "confidence": float between 0 and 1 (how confident you are the extraction is complete and accurate)

Text: {text}

Return ONLY valid JSON, no markdown."""

REFINED_PROMPT = """The previous extraction may have missed some triples or been inaccurate.
Please carefully re-read the text and extract ALL knowledge triples (subject, relation, object).
Be thorough - look for implicit relationships too.

Text: {text}

Previous attempt found: {previous}

Return a JSON object with:
- "triples": list of {{"subject": str, "relation": str, "object": str}}
- "confidence": float between 0 and 1

Return ONLY valid JSON, no markdown."""

MAX_ITERATIONS = 3
CONFIDENCE_THRESHOLD = 0.7


def run_agent_loop(text: str) -> dict:
    """
    Run the agent loop to extract knowledge triples from text.
    运行智能体循环，从文本中抽取知识三元组。

    Returns: {"triples": [...], "logs": [...]}
    """
    logs: list[str] = []
    triples = []
    iteration = 0

    while iteration < MAX_ITERATIONS:
        iteration += 1
        logs.append(f"=== Iteration {iteration}/{MAX_ITERATIONS} ===")

        # ─── Step 1: PERCEIVE (感知) ───
        # The agent receives and preprocesses the input
        logs.append(f"[Perceive] Input text: '{text[:80]}...' " if len(text) > 80 else f"[Perceive] Input text: '{text}'")

        # ─── Step 2: THINK (思考) ───
        # The agent decides what to do - here it calls the LLM
        if iteration == 1:
            prompt = EXTRACTION_PROMPT.format(text=text)
        else:
            prompt = REFINED_PROMPT.format(text=text, previous=json.dumps(triples, ensure_ascii=False))
        logs.append(f"[Think] Using {'initial' if iteration == 1 else 'refined'} prompt for extraction")

        # ─── Step 3: ACT (行动) ───
        # The agent executes its plan - calling the LLM API
        logs.append("[Act] Calling LLM to extract triples...")
        try:
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            raw = response.choices[0].message.content.strip()
            logs.append(f"[Act] LLM response received ({len(raw)} chars)")
        except Exception as e:
            logs.append(f"[Act] ERROR: LLM call failed: {e}")
            break

        # ─── Step 4: OBSERVE (观察) ───
        # The agent evaluates the result and decides whether to loop again
        try:
            result = json.loads(raw)
            triples = result.get("triples", [])
            confidence = result.get("confidence", 0.0)
            logs.append(f"[Observe] Extracted {len(triples)} triples, confidence: {confidence:.2f}")
        except json.JSONDecodeError:
            logs.append(f"[Observe] Failed to parse JSON, will retry")
            confidence = 0.0

        # Decision: continue loop or stop? (决策：继续循环还是停止？)
        if confidence >= CONFIDENCE_THRESHOLD:
            logs.append(f"[Observe] Confidence >= {CONFIDENCE_THRESHOLD}, stopping loop ✓")
            break
        else:
            logs.append(f"[Observe] Confidence < {CONFIDENCE_THRESHOLD}, will retry with refined prompt")

    # Store results in graph (将结果存入图)
    for t in triples:
        graph_store.add_triple(t["subject"], t["relation"], t["object"])
    logs.append(f"Stored {len(triples)} triples in graph.")

    return {"triples": triples, "logs": logs}
