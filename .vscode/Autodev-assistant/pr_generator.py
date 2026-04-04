def generate_pr(input_text, decision, code):
    target_file = "app.py"
    if decision.get("template") == "login_api":
        target_file = "login.py"
    elif decision.get("template") == "bug_fix":
        target_file = "fix_bug.py"
    elif decision.get("template") == "refactor":
        target_file = "refactor.py"

    title = f"{(decision.get('type') or 'Task').capitalize()} - Auto Generated Code"

    pr = f"""
=== PULL REQUEST ===

Title:
{title}

Description:
{input_text}

Files Changed:
- {target_file}

Generated Code:
{code.strip()}

Notes:
- Review the generated implementation and adjust as needed.
- The code is scaffolded from a template based on the detected task type.

====================
"""
    return pr
