from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import logging

from handlers import MyHandlers
from strings import APP_TOKEN


def initialize():
    """
    Create an updater and get dispatcher for that updater
    and add handler to dispacther
    """
    updater = Updater(token=APP_TOKEN)

    dispatcher = updater.dispatcher

    my_handler = MyHandlers()

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    start_handler = CommandHandler('start', my_handler.start)
    dispatcher.add_handler(start_handler)

    image_handler = CommandHandler('image', my_handler.image)
    dispatcher.add_handler(image_handler)

    echo_handler = MessageHandler(Filters.text, my_handler.echo)
    dispatcher.add_handler(echo_handler)
    return updater

bot = initialize()
bot.start_polling()
