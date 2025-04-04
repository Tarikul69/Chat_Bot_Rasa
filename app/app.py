from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_msg = request.form.get("message")
    payload = {"sender": "user", "message": user_msg}
    res = requests.post(RASA_URL, json=payload)
    bot_responses = res.json()
    reply = " ".join([r.get("text", "") for r in bot_responses])
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=8000)
