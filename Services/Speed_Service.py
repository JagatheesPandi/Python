class SpeedService:
    @staticmethod
    def get_speed_Service(words, time_taken):
        total_words = len(words.split())

        total_min = time_taken / 60
        if total_min == 0:
            return 0
        return total_words /total_min

