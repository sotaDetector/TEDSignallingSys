from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from sigSys.sigServiceCore import sigServiceCore

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
socketio = SocketIO(app, cors_allowed_origins="*")

sigService = sigServiceCore()


@socketio.on('join')
def OnJoin(data):
    sigService.OnJoin(data)


@socketio.on("message")
def OnMessage(data):
    sigService.OnMessage(data)


@socketio.on('leave')
def OnLeave(data):
    sigService.OnLeave(data)


def runScoketIo():
    socketio.run(app, host="0.0.0.0", port=3660)
    print("start socket io successfully...")


if __name__ == '__main__':
    runScoketIo()
