from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log',
    )


def start_button(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет {0}! Ты написал: {1}'.format(
        update.message.chat.first_name, update.message.text,)
    logging.info(
        'User: %s, Cchat id: %s, Message %s',
        update.message.chat.username,
        update.message.chat.id,
        update.message.text,
        )
    update.message.reply_text(user_text)


def main():
    mybot = Updater(
        settings.API_KEY, request_kwargs=settings.PROXY,)
    logging.info('Бот запускается...')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start_button))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()
