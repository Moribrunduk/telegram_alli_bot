import telebot
import Parsing_dollar
import Parsing_weather
bot = telebot.TeleBot("5300737902:AAHWfngF7lOD8bRHqOTZjrXM9QklbILAhD4")
name =""
sername = ""
age = 0
city = ""

Commands  = {"Курс": "позволяет увидеть курс валюты ", "Погода":"позволяет увидеть погоду в выбранном огороде", "Комплимент": "комплимент",}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	for key,value in Commands.items():
		bot.send_message(message.from_user.id,'__'+key+'__' + " \- " + value, parse_mode='MarkdownV2')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == 'Привет':
		bot.reply_to(message, 'Привет, подскажи, что бы ты хотел увидеть')
	elif message.text == "Рег":
		bot.send_message(message.from_user.id, 'Привет, давай познакомимся, как тебя зовут')
		bot.register_next_step_handler(message, reg_name)
	elif message.text == "Курс":
		bot.send_message(message.from_user.id, "Курс доллара ЦБ"+"\n"+"1 доллар = " + Parsing_dollar.From_CB() + " руб")
		bot.send_message(message.from_user.id, "Курс доллара Алиекспресс"+"\n"+"1 доллар = " + Parsing_dollar.From_Aliexpress() + " руб")
	elif message.text == "Комплимент":
		bot.send_message(message.from_user.id, Parsing_dollar.Love_words())
	elif message.text == "Погода":
		bot.send_message(message.from_user.id, 'Напиши название города')
		bot.register_next_step_handler(message, weather)

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
	pass
	global age
	age = int(message.text)
	if age != int:
		bot.send_message(message.from_user.id, 'Пиши цифрами')


def weather(message):
	global city
	city = message.text
	bot.send_message(message.from_user.id, Parsing_weather.Weather(city))

bot.infinity_polling()