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

print("Bot berjalan...")
bot.infinity_polling()
