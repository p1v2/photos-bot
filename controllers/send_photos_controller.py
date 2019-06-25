import settings
from controllers.base_controller import BaseController
from services.photo_sender import fetch_and_send_photo


class SendPhotosController(BaseController):
    def process(self):
        """
        Extracts hash tag from the message text and sends photos
        that contains the hash tab
        """
        hash_tag = self.request.text or settings.FALLBACK_TEXT
        text = f"💡 Here is what I found for you. Want to receive daily photos of **{hash_tag}**?\n"
        f"Click on **Subscribe** button."
        replies = ["Subscribe", f"One more {hash_tag} photo"]

        # Sends respective photo to user
        fetch_and_send_photo(self.request.chat_id, hash_tag, text, replies)
