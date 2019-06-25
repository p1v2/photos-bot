from controllers.base_controller import BaseController
from models.user import User
from telegram_api import send_text


class SubscriptionsController(BaseController):
    """
    Processes subscribe message
    """
    def process(self):
        user = User.get(chat_id=self.request.chat_id)

        # Get subscription work as a last search work
        user.subscription_word = user.last_search_word

        text = f"Cool 😎.\n"
        text += f"Now you will receive top **{user.subscription_word}** photos every day 👌.\n"
        text += f"Stay in touch!"

        # Send confirmation message
        send_text(self.request.chat_id, text)
