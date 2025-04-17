from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5055/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    try:
        user_message = request.form.get("message")
        response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
        response_data = response.json()
        bot_reply = " ".join([r.get("text", "") for r in response_data])
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host= '192.168.26.186', port=8000)
