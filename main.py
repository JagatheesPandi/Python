import time



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentence = " Python is fun and easy to learn"

    print("=" * 25)
    print(" Type the Sentence here")
    print("=" * 25)
    print(sentence)

    print("\nType the following Sentence\n")

    input("\nPress enter when is ready ...")
    start_time = time.time()
    typed_text = input("\n Start typing here : ")
    end_time = time.time()
    time_taken = end_time - start_time

    total_len = len(typed_text.split())
    total_mins = time_taken / 60
    total_time_taken = total_len / total_mins

    count = 0
    original_words = sentence.split()

    typed_words = typed_text.split()
    for i in range(len(typed_words)):

        if original_words[i] == typed_words[i]:
            count +=1
    accuracy = count / len(original_words) * 100

    print(f'Time take {time_taken : .2f}')
    print(f'Speed of word per minutes {total_time_taken : .2f} wpm')
    print(f'Accuracy : {accuracy}')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
