import telebot

TOKEN = "8860213176:AAHjSfPmtsB_RZbSrNMCDDx5A67gH-7M3HA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['pl'])
def premium_list(message):
    text = """
✨ LIST APLIKASI PREMIUM BY ALDIMEDIGITAL ✨

✧ alightmotion
✧ amazonprime
✧ applemusic
✧ bstation
✧ camscanner
✧ canva
✧ capcut
✧ chatgpt
✧ crunchyroll
✧ disney
✧ drakorid
✧ dramabox
✧ duolingo
✧ fizzo
✧ gagaoolala
✧ gemini
✧ grammarly
✧ grokai
✧ hbo
✧ ibispaintx
✧ ilovepdf
✧ iqiyi
✧ leonardoai
✧ lightroom
✧ loklok
✧ melolo
✧ microsoft365
✧ moviebox
✧ netflix
✧ nokos
✧ perplexity
✧ reelshort
✧ remini
✧ scribd
✧ teleprem
✧ vidio
✧ vision
✧ viu
✧ wattpad
✧ wetv
✧ wibuku
✧ wink
✧ youtube
✧ zoom
"""
    bot.reply_to(message, text)

@bot.message_handler(commands=['alightmotion'])
def alightmotion(message):
    text = """
Alight Motion

*SHARING*
↳ 1 Bulan : 3,500
↳ 3 Bulan : 5,500
↳ 1 Tahun : 7,500

▸ Private
↳ 1 Tahun : 9,000
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(commands=['amazonprime'])
def amazonprime(message):
    text = """
Amazon Prime

*SHARING*
↳ 4U 1 Bulan : 8.000
↳ 3U 1 Bulan : 9.000
↳ 2U 1 Bulan : 10.000

▸ Private
↳ 1 Month : 13.000
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(commands=['applemusic'])
def applemusic(message):
    text = """
Apple Music

*Sharing Premium ( Famplan invite )*
↳ 1 Bulan : 8.000
↳ 3 Bulan : 10.000

▸ Private Premium
↳ Head 1 Bulan : 10.000
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(commands=['bstation'])
def bstation(message):
    text = """
Bstation

*Sharing*
↳ 1 Month : 8.000
↳ 3 Month : 10.000
↳ 1 Year : 15.000

▸ Private
↳ 1 Month : 35.000
"""
    bot.reply_to(message, text, parse_mode='Markdown')

@bot.message_handler(commands=['camscanner'])
def camscanner(message):
    text = """
CamScanner

*Sharing*
↳ 1 Bulan : 8.000
↳ 1 Tahun : 15.000
"""
    bot.reply_to(message, text, parse_mode='Markdown')



print("Bot berjalan...")
bot.infinity_polling()
