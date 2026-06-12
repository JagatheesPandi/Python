import csv
import logging


class LeaderBoardService:
    @staticmethod
    def report():
        try:
            with open('reports/score_report.csv', 'r') as file:
                reader = csv.DictReader(file)
                #ls = list(reader)
                #ls.sort(key=lambda x : float(x['speed']), reverse= True)
                data = sorted(reader, key=lambda x : float(x['speed']), reverse= True)

                print("\n Top Score")
                for row in data[:5]:
                    print(f"{row['name']} | {row['speed']}")
        except FileNotFoundError:
            logging.ERROR("File Not Found")