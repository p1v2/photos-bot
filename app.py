import os

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def message():
    print(request)


if __name__ == '__main__':
    app.run(port=os.environ['PORT'], debug=True)
