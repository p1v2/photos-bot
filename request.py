import json
import logging


class Request:
    """
    A set of methods for better request processing
    """
    def __init__(self, flask_request):
        logging.warning(flask_request)
        logging.warning(flask_request.args)
        logging.warning(flask_request.data)
        self.body = json.loads(flask_request.data.decode('utf-8'))

    @property
    def chat_id(self):
        """
        Returns telegram chat id
        """
        return self.body["message"]["chat"]["id"]

    @property
    def first_name(self):
        """
        Returns first name of the user
        """
        return self.body["message"]["from"].get("first_name") or ''  # '' is a fallback first name

    @property
    def text(self):
        """
        Returns message text
        """
        return self.body["message"].get("text")

