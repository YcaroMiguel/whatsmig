from flask import Flask, request, session
from flask_socketio import SocketIO, send
from users import USERS

app = Flask(__name__)
app.secret_key = "chatseguro"
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = data.get("user")
    password = data.get("password")

    if user in USERS and USERS[user] == password:
        return {"status": "ok"}
    return {"status": "erro"}

@socketio.on("message")
def handle_message(msg):
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
