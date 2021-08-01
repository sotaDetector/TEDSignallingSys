from flask_socketio import emit

from commonUtils.logManager import logUtils


class socketService:

    # send msg to all in the room bu self
    @staticmethod
    def send_to_other(eventType, roomId, data):
        emit(eventType,(roomId,data), room=roomId, include_self=False)
        logUtils.info("send_to_other:eventType=" + eventType + ",roomId=" + roomId + ",data=" + str(data))

    # send to self
    @staticmethod
    def send_to_self(eventType,roomId,data):
        emit(eventType, (roomId,data))
        logUtils.info("send_to_self eventType=" + eventType + ",data=" + str(data))

    # send to all
    @staticmethod
    def send_to_all(eventType, roomId, data):
        emit(eventType, (roomId,data), room=roomId)
        logUtils.info("send_to_all:eventType=" + eventType + ",roomId=" + roomId + ",data=" + str(data))
