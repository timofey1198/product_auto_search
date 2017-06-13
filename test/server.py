from flask import Flask
from flask import session
from flask import request
import simple_bot
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    html = """
        <html>
            <head></head>
            <body>
                <a href="first_bot" target="blank">BOT</a>
            </body>
        </html>
    """
    print(request.user_agent)
    return html

@app.route("/first_bot")
def first_bot():
    simple_bot.start()
    return "Error..."


if __name__ == '__main__':
    app.run()
