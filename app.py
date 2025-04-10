



from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send

app =Flask(__name__)
CORS(app)
io = SocketIO(app, cors_allowed_origins="*")

messages = []

@app.route("/")
def home():
    return render_template("chat.html")

@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg)
    emit('getMessage', msg, broadcast=True)

@io.on('message')
def message_handler(msg):
    send(messages)


if __name__ == '__main__':
    io.run(app, debug=True)