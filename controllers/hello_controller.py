import os

from controllers.base_controller import BaseController
from services.reply_keyboard import get_reply_keyboard
from telegram_api import send_text


class HelloController(BaseController):
    """
    Processes conversation start message ("/start")
    """

    def process(self):
        """
        Sends welcome text to user
        """
        welcome_text = "Welcome 🙌"

        welcome_text += f", {self.request.first_name}.\n"

        text = f"My name is {os.environ.get('NAME')} and I really know where to get the best photos.\n" \
               f"Type me any word and I will return a related photo.\n" \
               f"For example, try to type **sunset**."

        send_text(
            self.request.chat_id,
            text=welcome_text + text,
            reply_keyboard=get_reply_keyboard(["sunset"])
        )
