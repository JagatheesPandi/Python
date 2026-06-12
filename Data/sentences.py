import random

class SentenceProvider:
    def __init__(self):
        self.sentence = [
            "Python is fun and easy to learn",
            "Automation testing improves software quality",
            "Practice makes a programmer better",
            "Playwright is a modern automation framework",
            "Coding every day improves problem solving"

        ]

    def get_sentence(self):
        return random.choice(self.sentence)