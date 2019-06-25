import logging

import requests
import settings

API_HOST = 'https://api.telegram.org/bot'
API_URL = f"{API_HOST}{settings.TELEGRAM_TOKEN}/"


def send_photo(chat_id, photo_url):
    """
    Sends photo message to user
    :param chat_id: Chat id of the user
    :param photo_url: URL of the photo to send
    :return:
    """
    resp = requests.post(
        f"{API_URL}sendPhoto",
        json={"chat_id": chat_id, "photo": photo_url}
    )

    # Logging telegram response
    logging.warning(resp.content)


def send_text(chat_id, text, reply_keyboard=None):
    """
    Sends text message to user
    :param chat_id: Chat id of the user
    :param text: Text to send
    :param reply_keyboard: Telegram custom replies to attach
    :return:
    """

    params = {"chat_id": chat_id, "text": text}

    # Attaching reply keyboard
    if reply_keyboard:
        params["reply_markup"] = {"keyboard": reply_keyboard, "one_time_keyboard": True}

    # Send request to telegram
    resp = requests.post(
        f"{API_URL}sendMessage",
        json=params
    )

    # Logging telegram response
    logging.warning(resp.content)

