def decide(structured_data):
    intent = structured_data["intent"]
    keywords = structured_data["keywords"]

    decision = {
        "type": intent,
        "template": None
    }

    if intent == "feature":
        if "login" in keywords:
            decision["template"] = "login_api"

    elif intent == "bug":
        decision["template"] = "bug_fix"

    elif intent == "refactor":
        decision["template"] = "refactor"

    return decision