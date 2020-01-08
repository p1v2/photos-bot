import random
import traceback

from pony.orm import db_session

from face_recognition import get_count_of_faces
from instagram_api import get_image_urls_by_hash_tag
from models.db_connection import db
from models.user import User
from telegram_api import send_photo, send_text

db.generate_mapping()


def send_photo_to_user(user: User):
    """
    Sends photo to user related to the subscription
    :param user: User to send
    """

    if user.subscription_word:
        send_text(user.chat_id, f"Hello there 😜!\nIt is time to receive a daily **{user.subscription_word}** photo.")
        faces_on_image = None

        # Checking if there are faces on image
        while faces_on_image != False:
            photo_url = random.choice(get_image_urls_by_hash_tag(user.subscription_word))
            faces_on_image = get_count_of_faces(photo_url) != 0

        send_photo(user.chat_id, photo_url)


@db_session
def update_subscriptions():
    """
    Sends photos to the all users
    """
    # Iterate over all users
    for user in User.select():
        try:
            # Sending photos related to the subscription word
            send_photo_to_user(user)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    update_subscriptions()
