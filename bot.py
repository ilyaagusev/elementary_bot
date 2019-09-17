import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import starter
import handlers


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log',
)


def main():
    mybot = Updater(
        settings.API_KEY, request_kwargs=settings.PROXY,)
    logging.info('Бот запускается...')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', starter.start_button))
    dp.add_handler(MessageHandler(Filters.text, handlers.talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()
