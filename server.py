import socketio
from flask import Flask

sio = socketio.Server(cors_allowed_origins="*")
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@sio.event
def connect(sid, environ):
    print("Cliente conectado:", sid)

@sio.event
def message(sid, data):
    sio.emit("message", data)

if __name__ == "__main__":
    import eventlet
    eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 5000)), app)
