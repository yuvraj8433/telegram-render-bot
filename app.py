import os
from flask import Flask, request
from bot import telegram_app

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    await telegram_app.process_update(data)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
