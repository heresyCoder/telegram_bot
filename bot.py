import telebot
import config
import bot_logic


# Настраиваем соединение с нашим ботом
bot = telebot.TeleBot(config.token)

# Начало работы бота
@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, 'Приветствую! Введите текст для перемешивания')

# Запрос помощи
@bot.message_handler(commands=['help'])
def help_message(message):

    bot.send_message(message.chat.id, '*most helpful message you ever seen*')

# Бот отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True)
def echo_all(message):

    bot_logic.write_log(message)
    bot.send_message(message.chat.id, bot_logic.make_random(message.text))

# Запускаем бота
bot.polling()