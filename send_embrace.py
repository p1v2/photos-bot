import traceback

from pony.orm import db_session

from giphy_api import GiphyApiClient
from models.db_connection import db
from models.user import User
from telegram_api import send_photo, send_text

db.generate_mapping()


def send_embrace_to_user(user: User):
    """
    Sends embrace giphy to user with any subscription
    :param user: User to send
    """

    if user.subscription_word:
        send_text(user.chat_id, f"Hello there 😜!\nIt is time for a virtual embrace:")
        embrace_url = GiphyApiClient().get_random_gif_url('embrace')
        resp = send_photo(user.chat_id, embrace_url)
        print(resp)


@db_session
def send_embrace():
    """
    Sends embraces to the all users
    """
    # Iterate over all users
    for user in User.select():
        try:
            # Sending embraces
            send_embrace_to_user(user)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    send_embrace()
