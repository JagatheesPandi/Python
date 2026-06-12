import os
import csv

os.makedirs("reports", exist_ok=True)


class ReportService:
    FILE_NAME = "reports/score_report.csv"

    @classmethod
    def save_report(cls, score):
        file_exist = os.path.exists(cls.FILE_NAME)
        with open(cls.FILE_NAME, 'a', newline="") as file:
            writer = csv.writer(file)

            if not file_exist:
                writer.writerow(['name', 'speed', 'accuracy'])
            writer.writerow([score.user_name, score.speed, score.accuracy])
