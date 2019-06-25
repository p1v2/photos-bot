from pony.orm import Required, Optional

from models.db_connection import db


class User(db.Entity):
    """
    Store information about every user of the bot
    """
    chat_id = Required(int)
    last_search_word = Optional(str)
    subscription_word = Optional(str)
