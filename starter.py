import logging


def start_button(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)
