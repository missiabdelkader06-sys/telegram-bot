from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")
ADMIN_ID = 7544213362
TARGET_ID = 7544213362

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text
    if user.id == ADMIN_ID:
        await context.bot.send_message(
            chat_id=TARGET_ID,
            text=message
        )
    else:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"رسالة من {user.first_name}:\n{message}"
        )
        await update.message.reply_text("تم استلام رسالتك ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
