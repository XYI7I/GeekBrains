from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5465453492:AAGlpXO1KnV9u0rOFSVCSgG6-5txP2FIHoo").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()