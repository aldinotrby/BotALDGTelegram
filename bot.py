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

print("Bot berjalan...")
bot.infinity_polling()