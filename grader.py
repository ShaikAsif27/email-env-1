def grade(action, expected):
    score = 0.0

    if action["label"] == expected:
        score += 0.7

    if len(action["response"]) > 5:
        score += 0.3

    return min(score, 1.0)
