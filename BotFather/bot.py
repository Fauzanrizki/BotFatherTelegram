import telebot
api = '5652680882:AAHPMt1pL_vSOGuChfe99el3Kvs5bufjf7I'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'halo apa kabar??')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'apa yang bisa saya bantu??')

print('bot start running')
bot.polling()
