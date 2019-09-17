import logging


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
