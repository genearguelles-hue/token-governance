#!/usr/bin/env python3
"""
Prompt Loader / Test Runner
Financial Guidance Demo Entity

Runs test prompts in one of two modes:

- governed: uses system-prompt.md as the runtime Persona construct
- ungoverned: sends the same prompts without the Persona construct

Outputs mode-labeled Markdown and CSV run files with token-governance metrics.

Expected location:
  docs/demo-entities/financial-guidance/prompt_loader.py
or:
  implementation/demo-entities/financial-guidance/prompt_loader.py

Required neighboring files:
  system-prompt.md      # required for governed mode
  test-prompts.md       # required for all modes

Example usage:
  python prompt_loader.py --mode governed --max-prompts 3
  python prompt_loader.py --mode ungoverned --max-prompts 3
  python prompt_loader.py --mode governed --max-prompts 3 --dry-run
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    from openai import OpenAI
except ImportError:  # handled again in main, so dry-run can still work if package is absent
    OpenAI = None  # type: ignore[assignment]


BASE_DIR = Path(__file__).resolve().parent

SYSTEM_PROMPT_PATH = BASE_DIR / "system-prompt.md"
TEST_PROMPTS_PATH = BASE_DIR / "test-prompts.md"
RUNS_DIR = BASE_DIR / "runs"

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")


@dataclass
class TestPrompt:
    label: str
    prompt: str


def load_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text or ""))


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Financial Guidance Demo Entity prompts in governed or ungoverned mode."
    )
    parser.add_argument(
        "--mode",
        choices=["governed", "ungoverned"],
        default=os.getenv("PROMPT_MODE", "governed"),
        help="governed uses system-prompt.md; ungoverned omits the Persona construct. Default: governed.",
    )
    parser.add_argument(
        "--max-prompts",
        type=int,
        default=int(os.getenv("MAX_PROMPTS", "3")),
        help="Maximum prompts to run. Use 0 to run all prompts. Default: env MAX_PROMPTS or 3.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model. Default: env OPENAI_MODEL or {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=int(os.getenv("MAX_OUTPUT_TOKENS", "0")),
        help="Optional hard cap for output tokens. Use 0 for API default.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call the API. Generate placeholder responses to test parsing and file output.",
    )
    return parser.parse_args()


def call_model(
    *,
    client: "OpenAI",
    model: str,
    mode: str,
    system_prompt: Optional[str],
    user_prompt: str,
    max_output_tokens: Optional[int],
) -> str:
    kwargs: Dict[str, object] = {
        "model": model,
        "input": user_prompt,
    }

    if mode == "governed":
        kwargs["instructions"] = system_prompt or ""
    elif mode == "ungoverned":
        # Intentionally omit instructions to create an ungoverned baseline.
        pass
    else:
        raise ValueError(f"Unsupported mode: {mode}")

    if max_output_tokens is not None:
        kwargs["max_output_tokens"] = max_output_tokens

    response = client.responses.create(**kwargs)
    return response.output_text


def dry_run_response(mode: str, test: TestPrompt) -> str:
    return (
        f"[DRY RUN — {mode}] Placeholder response for {test.label}. "
        "No API call was made. This confirms prompt extraction, mode labeling, "
        "metric collection, and file output behavior."
    )


def write_run_header(
    md_file,
    *,
    timestamp: str,
    mode: str,
    model: str,
    max_prompts: int,
    total_prompts_available: int,
    prompts_run: int,
    max_output_tokens: Optional[int],
    dry_run: bool,
) -> None:
    md_file.write("# Financial Guidance Demo Entity Run Log\n\n")
    md_file.write(f"- Date: `{timestamp}`\n")
    md_file.write(f"- Mode: `{mode}`\n")
    md_file.write(f"- Model: `{model}`\n")
    md_file.write(
        f"- System prompt: `{SYSTEM_PROMPT_PATH if mode == 'governed' else 'NONE — ungoverned baseline'}`\n"
    )
    md_file.write(f"- Test prompts: `{TEST_PROMPTS_PATH}`\n")
    md_file.write(f"- Total prompts available: `{total_prompts_available}`\n")
    md_file.write(f"- Prompts run: `{prompts_run}`\n")
    md_file.write(f"- Max prompts setting: `{max_prompts}`\n")
    md_file.write(f"- Max output tokens: `{max_output_tokens if max_output_tokens is not None else 'API default'}`\n")
    md_file.write(f"- Dry run: `{dry_run}`\n\n")


def main() -> None:
    args = parse_args()

    if args.max_prompts < 0:
        raise ValueError("--max-prompts must be 0 or greater")

    if args.max_output_tokens < 0:
        raise ValueError("--max-output-tokens must be 0 or greater")

    if not args.dry_run:
        if OpenAI is None:
            print("Missing dependency: openai")
            print("Install it with: python -m pip install openai")
            sys.exit(1)

        if not os.getenv("OPENAI_API_KEY"):
            print("Missing OPENAI_API_KEY environment variable.")
            print("Set it first, for example:")
            print('  export OPENAI_API_KEY="your_api_key_here"')
            print("or on Windows PowerShell:")
            print('  $env:OPENAI_API_KEY="your_api_key_here"')
            sys.exit(1)

    system_prompt = load_text(SYSTEM_PROMPT_PATH) if args.mode == "governed" else None
    test_prompts_md = load_text(TEST_PROMPTS_PATH)
    prompts = extract_test_prompts(test_prompts_md)

    if not prompts:
        raise ValueError("No fenced ```text prompts found in test-prompts.md")

    if args.max_prompts == 0:
        prompts_to_run = prompts
    else:
        prompts_to_run = prompts[: args.max_prompts]

    max_output_tokens = args.max_output_tokens if args.max_output_tokens > 0 else None

    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    md_output = RUNS_DIR / f"run-{args.mode}-{timestamp}.md"
    csv_output = RUNS_DIR / f"run-{args.mode}-{timestamp}.csv"

    client = OpenAI() if not args.dry_run else None
    rows: List[Dict[str, object]] = []

    with md_output.open("w", encoding="utf-8") as md:
        write_run_header(
            md,
            timestamp=timestamp,
            mode=args.mode,
            model=args.model,
            max_prompts=args.max_prompts,
            total_prompts_available=len(prompts),
            prompts_run=len(prompts_to_run),
            max_output_tokens=max_output_tokens,
            dry_run=args.dry_run,
        )

        for index, test in enumerate(prompts_to_run, start=1):
            print(f"Running {index}/{len(prompts_to_run)} [{args.mode}]: {test.label}")

            error = ""
            try:
                if args.dry_run:
                    output_text = dry_run_response(args.mode, test)
                else:
                    output_text = call_model(
                        client=client,  # type: ignore[arg-type]
                        model=args.model,
                        mode=args.mode,
                        system_prompt=system_prompt,
                        user_prompt=test.prompt,
                        max_output_tokens=max_output_tokens,
                    )
            except Exception as exc:
                output_text = f"[ERROR] {type(exc).__name__}: {exc}"
                error = f"{type(exc).__name__}: {exc}"

            prompt_word_count = count_words(test.prompt)
            response_word_count = count_words(output_text)
            response_char_count = len(output_text)

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
            md.write("### Token Governance Metrics\n")
            md.write(f"- Prompt word count: `{prompt_word_count}`\n")
            md.write(f"- Response word count: `{response_word_count}`\n")
            md.write(f"- Response character count: `{response_char_count}`\n")
            md.write(f"- Error: `{error if error else 'none'}`\n\n")
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
                    "mode": args.mode,
                    "index": index,
                    "label": test.label,
                    "prompt": test.prompt,
                    "response": output_text,
                    "prompt_word_count": prompt_word_count,
                    "response_word_count": response_word_count,
                    "response_char_count": response_char_count,
                    "error": error,
                    "model": args.model,
                    "timestamp": timestamp,
                    "dry_run": args.dry_run,
                }
            )

    fieldnames = [
        "mode",
        "index",
        "label",
        "prompt",
        "response",
        "prompt_word_count",
        "response_word_count",
        "response_char_count",
        "error",
        "model",
        "timestamp",
        "dry_run",
    ]

    with csv_output.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\nRun complete.")
    print(f"Mode: {args.mode}")
    print(f"Prompts run: {len(prompts_to_run)}")
    print(f"Markdown log: {md_output}")
    print(f"CSV log: {csv_output}")


if __name__ == "__main__":
    main()
