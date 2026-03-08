import telebot
import os
import sys

# GitHub Secrets üzerinden token'ı çekiyoruz
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("HATA: TELEGRAM_TOKEN bulunamadı!")
    sys.exit(1)
else:
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "🚀 Conexus MasterSystem Aktif!\n\nCEO Murat Akkuş için otonom strateji süreci başlatıldı. Emrindeyim komutan!")

    @bot.message_handler(commands=['analiz'])
    def analiz_mesaji(message):
        bot.reply_to(message, "📊 Derbi Analizi Verisi: Osimhen Gol (40'), Sane Asist. Sistem stabil.")

    print("Bot başlatıldı, sinyal bekleniyor...")
    bot.infinity_polling()
