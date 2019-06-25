from controllers.base_controller import BaseController
from models.user import User
from services.photo_sender import fetch_and_send_photo


class OneMorePhotoController(BaseController):
    """
    Sends photo to user according to his last search
    """
    def process(self):
        # Getting user's last search
        user = User.get(chat_id=self.request.chat_id) or User(chat_id=self.request.chat_id)
        hash_tag = user.last_search_word

        # Sending reply
        text = "No problem 😊. Here is one more photo."
        replies = ["Subscribe", f"One more {hash_tag} photo"]
        fetch_and_send_photo(self.request.chat_id, hash_tag, text, replies)
