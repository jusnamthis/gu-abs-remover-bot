from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def remove_seq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    await update.message.reply_text(f'{remove_abv(update.message.text)}')


def remove_abv(msg, seq='abv'):
    seq_len = len(seq)
    while msg:
        index = msg.find(seq)
        if index == -1:
            break
        msg = msg[:index] + msg[index+seq_len:]
    return msg