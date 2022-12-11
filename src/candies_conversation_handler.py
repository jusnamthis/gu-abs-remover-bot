from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)
import candies


PLAY, WAIT, FINISH = range(3)


MAX_CANDIES_IN_ONE_STEP = 28
TOTAL_NUM_OF_CANDIES = 220

_current_num_of_candies = TOTAL_NUM_OF_CANDIES

_info_msg = f'Current amount of candies on the tables is: {_current_num_of_candies}\nMax amount of candies for one step: {MAX_CANDIES_IN_ONE_STEP}\nEnter value'


def init_candies_handler():
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start_game', start_game)
        ],

        states={
            PLAY: [MessageHandler(filters.TEXT, move)]
        },

        fallbacks = []
    )

    return conv_handler


async def start_game(update, _):
    hello_msg = f'Welcome!\nYour move!\n{_info_msg}'
    await update.message.reply_text(f'{hello_msg}')
    return PLAY


async def move(update, _):
    user_candies = int(update.message.text)
    msg_add_info = ''
    if user_candies > 28:
        user_candies = 28
        msg_add_info = '\nYou have entered too large value so we will assume that you have entered 28.\n'
    global _current_num_of_candies
    _current_num_of_candies -= user_candies
    if _current_num_of_candies <= 0:
        await update.message.reply_text(f'YOU WON! CANGRATULATIONS!')
        return ConversationHandler.END
    bot_candies = candies.get_bot_move(_current_num_of_candies)
    _current_num_of_candies -= bot_candies
    if _current_num_of_candies <= 0:
        await update.message.reply_text(f'BOT WON! TRY AGAIN!')
        return ConversationHandler.END
    await update.message.reply_text(f'{msg_add_info}Bot\'s move: {bot_candies}\nCandies on the table: {_current_num_of_candies}')
    return PLAY