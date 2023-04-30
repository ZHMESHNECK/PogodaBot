import telebot
import environ
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

env = environ.Env()
env.read_env('.env')

bot = telebot.TeleBot(env('TOKEN'))
owm = OWM(env('OWM'))
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ru'



@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        weather = observation.weather
        temp = weather.temperature('celsius')['temp']

        answer =  (" В городе " + message.text + " сейчас " + w.detailed_status)
        answer += (' температура '+ str(temp))

        if temp < 10:
            answer += (" очень холодно ")
        elif temp < 20:
            answer += (" слегка прохладно ")
        else:
            answer += (" погода как надо ")
        
        bot.send_message(message.chat.id, answer)
    except Exception:
        bot.send_message(message.chat.id, "Введен неверный город")
	
bot.infinity_polling()