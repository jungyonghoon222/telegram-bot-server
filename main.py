from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route('/', methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message", "No message provided.")
    
    if not TOKEN or not CHAT_ID:
        return {"error": "Missing TOKEN or CHAT_ID"}, 500
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    return {"ok": response.ok}, response.status_code

@app.route('/', methods=["GET"])
def index():
    return "Telegram bot server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
