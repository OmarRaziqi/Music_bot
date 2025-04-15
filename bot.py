import telebot
import requests

# توکن ربات تلگرامت ره اینجا بگذار
TOKEN = "توکن_ربات_خودت_اینجا"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "سلام! نام آهنگ ره بفرست تا پیدایش کنم.")

@bot.message_handler(func=lambda m: True)
def search_music(message):
    query = message.text
    bot.reply_to(message, f"در حال جستجو برای آهنگ: {query}")
    # اینجا می‌تانی API جستجوی آهنگ اضافه کنی

bot.polling()
