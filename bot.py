if user_id == ADMIN_CHAT_ID:
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        await update.message.reply_text(f"👥 عدد المستخدمين المسجلين: {count}")
    else:
        await update.message.reply_text("❌ هذا الأمر متاح فقط للأدمن.")

if name == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reset_data", reset_data))
    application.add_handler(CommandHandler("user_count", user_count))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

from telegram import version as tg_version
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# تحقق من إصدار المكتبة
print(f"Telegram Bot Library Version: {tg_version}")

API_TOKEN = "8154296863:AAEdjzVYyvndPdAkKlPZNw04Ep6bzRcsDxY"
ADMIN_CHAT_ID = 270734616  # معرف الأدمن

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"مرحبًا بك، معرفك هو: {user_id}")

# استقبال الرسائل
async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"أرسلت الرسالة: {user_message}")

if name == '__main__':
    # إنشاء التطبيق
    application = ApplicationBuilder().token(API_TOKEN).build()

    # إضافة الأوامر والمعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))

    # تشغيل البوت
    application.run_polling()