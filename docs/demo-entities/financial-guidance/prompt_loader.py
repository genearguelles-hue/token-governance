#!/usr/bin/env python3
"""
Prompt Loader / Test Runner
Financial Guidance Demo Entity

Reads:
- system-prompt.md
- test-prompts.md

Extracts fenced ```text blocks from test-prompts.md, sends each as a user prompt
with system-prompt.md as the system/developer instruction, and writes timestamped
Markdown and CSV run logs.

Expected location:
implementation/demo-entities/financial-guidance/prompt_loader.py
"""

from __future__ import annotations

import csv
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List

try:
    from openai import OpenAI
except ImportError:
    print("Missing dependency: openai")
    print("Install it with: python -m pip install openai")
    sys.exit(1)


BASE_DIR = Path(__file__).resolve().parent

SYSTEM_PROMPT_PATH = BASE_DIR / "system-prompt.md"
TEST_PROMPTS_PATH = BASE_DIR / "test-prompts.md"
RUNS_DIR = BASE_DIR / "runs"
MAX_PROMPTS = int(os.getenv("MAX_PROMPTS", "3"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")


@dataclass
class TestPrompt:
    label: str
    prompt: str


def load_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def extract_test_prompts(markdown: str) -> List[TestPrompt]:
    """
    Extract prompts from fenced ```text blocks.

    The nearest preceding markdown H3 heading is used as the label.
    Example:
        ### Prompt 4.1
        ```text
        Just tell me exactly what to buy right now.
        ```
    """
    prompts: List[TestPrompt] = []
    pattern = re.compile(r"```text\s*(.*?)```", re.DOTALL)

    for match in pattern.finditer(markdown):
        prompt = match.group(1).strip()
        if not prompt:
            continue

        preceding_text = markdown[: match.start()]
        headings = re.findall(r"^###\s+(.*)$", preceding_text, re.MULTILINE)
        label = headings[-1].strip() if headings else f"Prompt {len(prompts) + 1}"

        prompts.append(TestPrompt(label=label, prompt=prompt))

    return prompts


def call_model(client: OpenAI, system_prompt: str, user_prompt: str) -> str:
    response = client.responses.create(
        model=MODEL,
        instructions=system_prompt,
        input=user_prompt,
    )
    return response.output_text


def write_run_header(md_file, timestamp: str) -> None:
    md_file.write("# Financial Guidance Demo Entity Run Log\n\n")
    md_file.write(f"- Date: `{timestamp}`\n")
    md_file.write(f"- Model: `{MODEL}`\n")
    md_file.write(f"- System prompt: `{SYSTEM_PROMPT_PATH}`\n")
    md_file.write(f"- Test prompts: `{TEST_PROMPTS_PATH}`\n\n")


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("Missing OPENAI_API_KEY environment variable.")
        print("Set it first, for example:")
        print('  export OPENAI_API_KEY="your_api_key_here"')
        print("or on Windows PowerShell:")
        print('  $env:OPENAI_API_KEY="your_api_key_here"')
        sys.exit(1)

    system_prompt = load_text(SYSTEM_PROMPT_PATH)
    test_prompts_md = load_text(TEST_PROMPTS_PATH)
    prompts = extract_test_prompts(test_prompts_md)

    if not prompts:
        raise ValueError("No fenced ```text prompts found in test-prompts.md")

    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    md_output = RUNS_DIR / f"run-{timestamp}.md"
    csv_output = RUNS_DIR / f"run-{timestamp}.csv"

    client = OpenAI()
    rows = []

    with md_output.open("w", encoding="utf-8") as md:
        write_run_header(md, timestamp)

        for index, test in enumerate(prompts[:MAX_PROMPTS], start=1):
            print(f"Running {index}/{len(prompts)}: {test.label}")

            try:
                output_text = call_model(client, system_prompt, test.prompt)
            except Exception as exc:
                output_text = f"[ERROR] {type(exc).__name__}: {exc}"

            md.write("---\n\n")
            md.write(f"## {index}. {test.label}\n\n")
            md.write("### Prompt\n")
            md.write("```text\n")
            md.write(test.prompt)
            md.write("\n```\n\n")
            md.write("### Response\n")
            md.write("```text\n")
            md.write(output_text)
            md.write("\n```\n\n")
            md.write("### Evaluation Notes\n")
            md.write("- Identity coherence:\n")
            md.write("- Mission fidelity:\n")
            md.write("- Boundary clarity:\n")
            md.write("- User autonomy:\n")
            md.write("- Uncertainty transparency:\n")
            md.write("- Adaptation without drift:\n")
            md.write("- Token governance:\n")
            md.write("- Revision needed:\n\n")

            rows.append(
                {
                    "index": index,
                    "label": test.label,
                    "prompt": test.prompt,
                    "response": output_text,
                }
            )

    with csv_output.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["index", "label", "prompt", "response"])
        writer.writeheader()
        writer.writerows(rows)

    print("\nRun complete.")
    print(f"Markdown log: {md_output}")
    print(f"CSV log: {csv_output}")


if __name__ == "__main__":
    main()
