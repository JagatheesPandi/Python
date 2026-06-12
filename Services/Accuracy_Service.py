class AccuracySerivce:
    @staticmethod
    def get_accuracy(orgWords, typeWords):
        org = orgWords.split()
        typed = typeWords.split()
        counter = 0

        for i in range(len(typed)):
            if org[i] == typed[i]:
                counter += 1
        return counter / len(org) * 100

