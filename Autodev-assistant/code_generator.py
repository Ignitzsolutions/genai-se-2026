from templates import login_api, bug_fix, refactor

def generate_code(decision):
    template = decision.get("template")

    if template == "login_api":
        return login_api.get_code()

    elif template == "bug_fix":
        return bug_fix.get_code()

    elif template == "refactor":
        return refactor.get_code()

    return "# No template found"