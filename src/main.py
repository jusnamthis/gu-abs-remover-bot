from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    ContextTypes, 
    MessageHandler, 
    ConversationHandler, 
    filters
)
from bot_commands import hello, remove_seq
from candies_conversation_handler import init_candies_handler


if __name__ == '__main__':    
    app = ApplicationBuilder().token("PUT_YOUR_TOKEN_HERE").build()

    game_handler = init_candies_handler()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(game_handler)
    app.add_handler(MessageHandler(filters.TEXT, remove_seq))

    app.run_polling()