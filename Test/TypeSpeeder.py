from Data.sentences import *
from Services.Accuracy_Service import *
from Services.time_service import *
from Services.Speed_Service import *
from utils.console import *
from utils.logger import *
from models.Typing_test import *


class typeSpeeder:
    Console.print_header()
    sentence_prodiver = SentenceProvider()
    sentence = (sentence_prodiver.get_sentence())
    Console.print_sentence(sentence)
    input("\n Press Enter to start")
    timer = TimerSerivce()
    timer.startTimer()
    user_input = input("\n Start Typing : \n")
    timer.endTimer()

    elapsed_timer = (timer.get_elapsed_timer())
    speed = SpeedService()
    wpm = speed.get_speed_Service(user_input, elapsed_timer)
    acc = AccuracySerivce()
    acc_words = acc.get_accuracy(sentence, user_input)

    type_test = TypingTest(sentence, user_input, wpm, acc_words, elapsed_timer)
    type_test.print_results()
