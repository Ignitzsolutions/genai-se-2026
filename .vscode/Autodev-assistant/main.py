import argparse
from pathlib import Path

from input_understanding import process_input
from decision_engine import decide
from code_generator import generate_code
from pr_generator import generate_pr

DEFAULT_CODE_FILES = {
    "login_api": Path("login.py"),
    "bug_fix": Path("fix_bug.py"),
    "refactor": Path("refactor.py"),
}


def write_text_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def run(task_text: str, code_path: Path | None = None, pr_path: Path | None = None) -> None:
    structured = process_input(task_text)
    decision = decide(structured)
    code = generate_code(decision)
    pr = generate_pr(task_text, decision, code)

    print(pr)

    if code_path:
        write_text_file(code_path, code)
        print(f"Generated code written to: {code_path}")

    if pr_path:
        write_text_file(pr_path, pr)
        print(f"PR description written to: {pr_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Autodev assistant: generate code and PR content from a task description"
    )
    parser.add_argument(
        "--task", "-t",
        type=str,
        help="Task description to generate code and PR text for."
    )
    parser.add_argument(
        "--write-code", "-c",
        type=Path,
        help="Optional output path to save generated code."
    )
    parser.add_argument(
        "--write-pr", "-p",
        type=Path,
        help="Optional output path to save generated PR description."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    task_text = args.task

    if not task_text:
        task_text = input("Enter your task: ").strip()

    if not task_text:
        raise SystemExit("A task description is required.")

    code_path = args.write_code
    if code_path is None:
        decision = decide(process_input(task_text))
        template = decision.get("template")
        code_path = DEFAULT_CODE_FILES.get(template)

    run(task_text, code_path=code_path, pr_path=args.write_pr)
