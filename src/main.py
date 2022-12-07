from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from bot_commands import hello, remove_seq


app = ApplicationBuilder().token("PUT TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT, remove_seq))

app.run_polling()