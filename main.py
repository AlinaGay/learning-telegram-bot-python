import telebot

bot = telebot.TeleBot('7469506806:AAG19VsWcccnieJclR9kmtqBj8t7OdmO_fE')

@bot.message_handler(commands=['start'])
def start(message):
  mess = f'Привет, <b>{message.from_user.first_name}</b>'
  bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
  if message.text == "Hello!":
    bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
  elif message.text == "id":
    bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
  else:
    bot.send_message(message.chat.id, "Я тебя не понимаю!", parse_mode='html')

bot.polling(non_stop=True) 