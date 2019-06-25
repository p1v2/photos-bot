import os
import traceback

from flask import Flask, request as flask_request
from pony.orm import db_session

from controllers.hello_controller import HelloController
from controllers.one_more_photo_controller import OneMorePhotoController
from controllers.send_photos_controller import SendPhotosController
from controllers.subscriptions_controller import SubscriptionsController

from request import Request

from models.db_connection import db
from telegram_api import send_text

# Create relations between models classes and db tables
db.generate_mapping(create_tables=True, check_tables=True)

# Flask web app
app = Flask(__name__)


@app.route('/', methods=['post'])
@db_session
def message():
    request = Request(flask_request)

    # Processing message here
    try:
        # Hello message
        if request.text == '/start':
            HelloController(request).process()
        # Subscribe message
        elif request.text.lower() == "subscribe":
            SubscriptionsController(request).process()
        # One more message
        elif request.text.lower().startswith("one more"):
            OneMorePhotoController(request).process()
        # Sends photos message
        else:
            SendPhotosController(request).process()
    except:
        traceback.print_exc()
        # If something went totally wrong, send callback message
        send_text(request.chat_id, "Sorry, I'm broken!")

    return "OK"


if __name__ == '__main__':
    # Starting flask app here
    app.run(host='0.0.0.0', port=os.environ['PORT'], debug=True)
