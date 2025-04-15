from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ذخیره زبان انتخابی کاربران
user_languages = {}

# دکمه انتخاب زبان
language_keyboard = ReplyKeyboardMarkup(
    [['فارسی', 'English']],
    resize_keyboard=True,
    one_time_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "لطفاً زبان خود را انتخاب کنید:\nPlease choose your language:",
        reply_markup=language_keyboard
    )

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.lower()

    if text in ['فارسی', 'farsi', 'persian']:
        user_languages[user_id] = 'fa'
        await update.message.reply_text("زبان شما فارسی تنظیم شد. حالا نام آهنگ را بفرست.")
    elif text == 'english':
        user_languages[user_id] = 'en'
        await update.message.reply_text("Your language is set to English. Now send the song name.")
    else:
        await update.message.reply_text("زبان نامعتبر است. لطفاً یکی از گزینه‌ها را انتخاب کنید.")

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, 'fa')  # پیش‌فرض فارسی

    query = ' '.join(context.args)
    if query:
        if lang == 'fa':
            await update.message.reply_text(f"در حال جستجو برای: {query}\n(لینک دانلود نمونه)")
        else:
            await update.message.reply_text(f"Searching for: {query}\n(Sample download link)")
    else:
        if lang == 'fa':
            await update.message.reply_text("لطفاً نام آهنگ را وارد کن.")
        else:
            await update.message.reply_text("Please enter the song name.")

# راه‌اندازی بات
app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("music", music))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_language))

app.run_polling()
