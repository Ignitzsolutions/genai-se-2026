def process_input(text):
    text = text.lower()

    data = {
        "raw": text,
        "keywords": [],
        "intent": None
    }

    # Keyword extraction (simple)
    if "login" in text:
        data["keywords"].append("login")

    if "api" in text:
        data["keywords"].append("api")

    if "bug" in text or "fix" in text:
        data["intent"] = "bug"

    elif "create" in text or "add" in text:
        data["intent"] = "feature"

    elif "refactor" in text:
        data["intent"] = "refactor"

    return data