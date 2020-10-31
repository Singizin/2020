import flask

import os

import flask
import json

from flask import render_template


app = flask.Flask(__name__)


@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    json_data = flask.request.json
    print(json_data)
    return json.dumps({'success': True})


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    app.run(debug=True)