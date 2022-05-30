import time
import random
import telebot
import threading
from telebot import types


bot = telebot.TeleBot('5367342484:AAHm8YnLLAkJn4yGyVfIhxrARJECFn42MMA')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'


    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("Рандомное число")
    key2 = types.KeyboardButton("whatsup")

    markup.add(key1, key2)

    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_mess(message):
    if message.from_user.username == 'ArnellaSaifieva':
        message.text = 'Привет, Арнелла!'
        bot.send_message(message.chat.id, message.text, parse_mode='html')
    if message.text == 'whatsup':
        markup = types.InlineKeyboardMarkup(row_width=2)
        key1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
        key2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

        markup.add(key1, key2)

    bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько!')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает(')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='.', reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.message.chat.id, show_alert=False, text='Это тестовое уведомление')

    except Exception as e:
        print(repr(e))
# @bot.message_handler(content_types=['text'])
# def whatsup(message):


bot.polling(none_stop=True)
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#
#     nums = int(message.text)
#     a = []
#     text_all = ''
#     for i in range(int(nums)):
#         numerator = random.randint(50, 300)
#         denominator = random.randint(2, 50)
#         a.append(numerator)
#         a.append(denominator)
#         text = str(numerator) + "/" + str(denominator)
#         text_all += text +'\n'
#     bot.send_message(message.chat.id, text_all)
#     time.sleep(10)
#     result_all = ''
#     for i in range(len(a)):
#         if i % 2 == 0:
#             result = a[i] // a[i + 1]
#             result = str(result)
#             if a[i] % a[i + 1] != 0:
#                 result = result + ' +' + str(a[i] % a[i + 1]) + '/' + str(a[i + 1])
#             else:
#                 result += ''
#             result_all += result + '\n'
#     bot.send_message(message.chat.id, result_all)

# if message.text == "Hello":
    #     bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#threading.Thread(target=get_user_text, args=(1,), daemon=True).start()


        # print(numerator, "/", denominator)
    # temp = input("Проверить?\n")
    # if temp == "да":
    #     for i in range(len(a)):
    #         if i % 2 == 0:
    #             print(a[i] // a[i + 1], end='')
    #             if a[i] % a[i + 1] != 0:
    #                 print(" +", a[i] % a[i + 1], "/", a[i + 1])
    #             else:
    #                 print()

# @bot.message_handler(commands=['buttons'])
# def buttons(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     task_5 = types.KeyboardButton('5')
#     task_10 = types.KeyboardButton('10')
#     task_15 = types.KeyboardButton('15')

# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     website = types.KeyboardButton('Веб сайт')
#     start = types.KeyboardButton('start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('icon.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, "Вау! Крутое фото!")
#
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.google.ru/"))
#     bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)






#bot.sleep()