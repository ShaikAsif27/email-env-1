def baseline_agent(obs):
    text = obs["email_text"].lower()

    if "win" in text:
        return {"label": "spam", "response": "Ignored spam"}
    elif "urgent" in text or "asap" in text:
        return {"label": "urgent", "response": "Working on it"}
    else:
        return {"label": "normal", "response": "Noted"}
