from strings import GOOGLE_CUSTOM_SEARCH_URL
import requests


class MyHandlers(object):

    def start(self, bot, update):
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Hi, human, I'm a bot Please Talk to me"
        )

    def echo(self, bot, update):
        bot.send_message(
            chat_id=update.message.chat_id,
            text=update.message.text
        )

    def image(self, bot, update):
        query_param = update.message.text.replace('/image', '').strip()
        image_data = requests.get(GOOGLE_CUSTOM_SEARCH_URL.replace('query_param', query_param))
        if image_data.ok:
            image_data = image_data.json()
            image_data['items'][0]['link']
            bot.send_photo(chat_id=update.message.chat_id, photo=image_data['items'][0]['link'])
