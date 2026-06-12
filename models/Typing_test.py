class TypingTest:

    def __init__(self, sentence, userinput,speed, accuracy, timeelpased):
        self.sentence = sentence
        self.userinput = userinput
        self.speed = speed
        self.accuracy = accuracy
        self.timeelpased = timeelpased

    def print_results(self):
        print("\n Results")

        print(f"Time Elasped {self.timeelpased : .2f}")

        print(f'Word Per Minutes {self.speed} wpm')

        print(f'Accuracy of words {self.accuracy}')