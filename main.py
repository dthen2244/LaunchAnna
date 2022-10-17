import telebot
from telebot import types

bot: telebot.TeleBot = telebot.TeleBot('5752879311:AAH8ALBBtw5dolSNJeJ34mPkASan6_Zf_2E')


def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=True)
    link_keyboard = types.InlineKeyboardButton(text="Подписаться✅", url="https://t.me/anykonn")
    check_keyboard = types.InlineKeyboardButton(text="Продолжить➡️", callback_data="check")
    markup.add(link_keyboard, check_keyboard)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"Привет {first_name} !\n"
                              f"(Здесь будет неебичиский прогрев к статье) Чтобы продолжить подпишись на канал!",
                     reply_markup=start_markup())


def cheсk(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id="-1001719693666", user_id=call.message.chat.id).status:
            bot.send_message(call.message.chat.id, "Здесь будет неебическая статья!")
            break

    else:
        bot.send_message(call.message.chat.id, "Подпишитесь на канал!", reply_markup=start_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'check':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        cheсk(call)


@bot.message_handler(commands=['article'])
def open_article(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Прочитать статью", url="https://www.google.ru/"))
    bot.send_message(message.chat.id, 'Вот ссылка', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['telegram'])
def telegram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Написать мне", url="https://t.me/anykon1"))
    bot.send_message(message.chat.id, "Нажми чтобы перейти", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['channel'])
def channel(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Зайти на канал", url="https://t.me/anykonn"))
    bot.send_message(message.chat.id, "Нажми чтобы перейти", parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
