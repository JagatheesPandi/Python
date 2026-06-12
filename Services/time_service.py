import time


class TimerSerivce:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def startTimer(self):
        self.start_time = time.time()

    def endTimer(self):
        self.end_time = time.time()

    def get_elapsed_timer(self):
        return self.end_time - self.start_time
