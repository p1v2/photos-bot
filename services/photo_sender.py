import logging
import random
import traceback

from giphy_api import giphy_client
from instagram_api import get_image_urls_by_hash_tag
from models.user import User
from services.reply_keyboard import get_reply_keyboard
from telegram_api import send_photo, send_text


def fetch_and_send_photo(chat_id, hash_tag, text, replies):
    """
    Sends a photo from instagram to user by specified hashtag
    :param chat_id: User's telegram chat id
    :param hash_tag: Hashtag to fetch photo from instagram
    :param text: Additional text to send after sending photo
    :param replies: Telegram keyboard replies
    :return:
    """
    logging.warning(f"Fetching photo with hashtag: {hash_tag}")
    try:
        # Getting url for the instagram photo
        photo_url = random.choice(get_image_urls_by_hash_tag(hash_tag))

        # Send photo
        send_photo(chat_id, photo_url)

        # Send text message after photo
        send_text(chat_id, text,
                  reply_keyboard=get_reply_keyboard(replies))

        # Get or create user record in DB
        user = User.get(chat_id=chat_id) or User(chat_id=chat_id)
        # Update user record with the last search word
        user.last_search_word = hash_tag

    except:
        traceback.print_exc()
        # Something went wrong with the instagram
        response_text = "👺 Instagram sucks. I will show you some gif on a meantime."

        # Fetching url from giphy
        gif_url = giphy_client.get_random_gif_url(text)

        # Sending giphy url
        send_text(chat_id, f"{response_text}\n{gif_url}")
