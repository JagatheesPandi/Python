from config.config_loader import *

from Data.sentences import *

from models.score import *
from models.Typing_test import *

from Services.Accuracy_Service import *
from Services.time_service import *
from Services.Speed_Service import *
from Services.report_service import *
from Services.leaderboard_service import *

from utils.logger import *
from utils.console import *
from utils.validator import *
from utils.pathManager import *
import json


class TypeSpeeder_Enterpise:
    try:
        import os

        print(os.getcwd())
        Logger.info("Application Started")

        # Load Config
        config = JsonLoader.load()
        Console.print_header()

        # Usernmae
        user_name = input("\n Enter Name")
        Validator.valid_name(user_name)
        Logger.info(f"User name {user_name}")

        # Get Sentence
        sentence = SentenceProvider()
        original_sentence = sentence.get_sentence()
        Console.print_sentence(original_sentence)

        input("\n Press Enter here")
        timer = TimerSerivce()
        timer.startTimer()

        user_input = input("\n Enter Sentence here :")
        timer.endTimer()

        elapsed_time = timer.get_elapsed_timer()

        # Speed Calculator

        speed = SpeedService()
        speed_calc = speed.get_speed_Service(user_input, elapsed_time)

        # Accuracy
        _accuracy = AccuracySerivce()
        acc_calc = _accuracy.get_accuracy(original_sentence, user_input)

        Logger.info(f"Speed {speed_calc : .2f}" f"Accuracy {acc_calc :.2f} wpm")

        typingtest = TypingTest(original_sentence, user_input, speed_calc, acc_calc, elapsed_time)
        typingtest.print_results()

        score = Score(user_name, speed_calc, acc_calc)
        ReportService.save_report(score)

        Logger.info("Report is Saved")

        # Min Accuracy
        min_acc = config['min_accuracy']

        if acc_calc < min_acc:
            print(f"\n Below Accuracy"
                  f"Below{acc_calc}%")
            Logger.info("Below Thershold")

        LeaderBoardService.report()
        Logger.info("Leader Board Displayed")
        Logger.info("Application Ended")
    except ValueError as e:
        Logger.error(str(e))
        print(f"\n error : {e}")
    except FileNotFoundError as e:
        Logger.error(f"\n File Not Found : {e}")
        print(f"\n file not found : {e}")
    except Exception as e:
        Logger.error(str(e))
        print(f"\n Error : {e}")
