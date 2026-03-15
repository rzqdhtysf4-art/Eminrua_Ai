import telebot

# റെയിൽവേയിലെ വേരിയബിളിൽ നിന്ന് ടോക്കൺ എടുക്കുന്നു
import os
TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ഹായ് ഷാനു! ഞാൻ എമി (Emi). നിന്റെ 3D പേഴ്സണൽ ലേണിംഗ് അസിസ്റ്റന്റ് റെഡിയാണ്! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "നീ പറഞ്ഞത് എനിക്ക് മനസ്സിലായി. നമുക്ക് ഉടനെ പഠിച്ചു തുടങ്ങാം!")

bot.infinity_polling()

