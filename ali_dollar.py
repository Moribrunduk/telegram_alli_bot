import telebot
import Parsing_dollar
bot = telebot.TeleBot("5300737902:AAHWfngF7lOD8bRHqOTZjrXM9QklbILAhD4")
name =""
sername = ""
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == 'Привет':
		bot.reply_to(message, 'Привет, подскажи, что бы ты хотел увидеть')
	elif message.text == "Рег":
		bot.send_message(message.from_user.id, 'Привет, давай познакомимся, как тебя зовут')
		bot.register_next_step_handler(message, reg_name)
	elif message.text == "Курс":
		print(Parsing_dollar.Dollar_rub)
		bot.send_message(message.from_user.id, "1 доллар = " + Parsing_dollar.Dollar_rub + " руб")
def reg_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'Какая у тебя фамилия')
	bot.register_next_step_handler(message, reg_sername)
def reg_sername(message):
	global sername
	sername = message.text
	bot.send_message(message.from_user.id, 'Сколько тебе лет')
	bot.register_next_step_handler(message, reg_age)
def reg_age(message):
	global age
	while age == 0:
		try:
			age = int(message.text)
			bot.send_message(message.from_user.id, 'збс')
		except TypeError:
			bot.send_message(message.from_user.id, 'Пиши циферами')
			age = 0
			bot.register_next_step_handler(message, reg_age)

bot.infinity_polling()