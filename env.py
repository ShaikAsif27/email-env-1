import random
from models import Observation
from tasks import get_task_emails
class EmailEnv:
    def __init__(self):
        self.level = "easy"
        self.emails = get_task_emails(self.level)
        self.current = None
        self.done = False
        self.current = None
        self.done = False

    def reset(self):
        self.current = random.choice(self.emails)
        self.done = False
        return {
            "email_text": self.current["text"],
            "sender": "user@example.com"
        }

    def step(self, action):
        correct = self.current["label"]
        reward = 0.0

        if action["label"] == correct:
            reward += 0.6
        else:
            reward -= 0.2

        if len(action["response"]) > 5:
            reward += 0.4

        self.done = True

        return {
            "observation": {
                "email_text": self.current["text"],
                "sender": "user@example.com"
            },
            "reward": reward,
            "done": self.done,
            "info": {"correct_label": correct}
        }

    def state(self):
        return self.current
