import random
import datetime


def shuffle_letters(word_list):
    "Перемешивание букв в слове. Начальная и конечная буквы остаются на местах"

    if len(word_list) < 4:

        return word_list

    word_list_cut = word_list[1:-1]
    for i in range(1000):

        word_try_shuffle = word_list_cut.copy()
        random.shuffle(word_try_shuffle)
        if word_try_shuffle != word_list_cut:

            word_list_cut = word_try_shuffle
            break

    return [word_list[0]] + word_list_cut + [word_list[-1]]


def make_random(text):
    "Обработка входного текста, возвращение перемешанного текста"

    result_list = []
    letter_list = []
    for symbol in text:

        if symbol.isalpha():

            letter_list.append(symbol)

        else:

            if len(letter_list):

                result_list += shuffle_letters(letter_list)
                letter_list.clear()

            result_list.append(symbol)

    if len(letter_list):

        result_list += shuffle_letters(letter_list)

    return ''.join(result_list)

def write_log(message):

    log_message = []
    # Конвертируем время и дату из Unix-формата в привычный вид
    date = datetime.datetime.fromtimestamp(message.date).strftime('%H:%M:%S %d-%m-%Y')

    log_message.append('-----------------------------------\n')
    log_message.append('from ' + message.from_user.first_name + ' at ' + date)
    log_message.append('\n-----------------------------------\n')
    log_message.append(message.text)
    log_message.append('\n')

    logfile = open('log.txt', 'a')
    logfile.write(''.join(log_message))
    logfile.close()
