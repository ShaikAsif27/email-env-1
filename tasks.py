def get_task_emails(level):
    if level == "easy":
        return [
            {"text": "Win money now!!!", "label": "spam"},
            {"text": "Server down ASAP", "label": "urgent"},
        ]

    elif level == "medium":
        return [
            {"text": "Meeting at 5pm", "label": "normal"},
            {"text": "Please review the document", "label": "normal"},
            {"text": "Urgent: submit report", "label": "urgent"},
        ]

    elif level == "hard":
        return [
            {"text": "Limited time offer just for you", "label": "spam"},
            {"text": "Can we reschedule?", "label": "normal"},
            {"text": "This needs attention soon", "label": "urgent"},
            {"text": "Congratulations, you’ve been selected", "label": "spam"},
        ]

    else:
        return []
