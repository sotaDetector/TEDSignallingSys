from flask_socketio import join_room, leave_room

from commonUtils.dataFlags import commonDataTag
from commonUtils.logManager import logUtils
from sigSys.socketMsgUtilsr import socketService



class sigDataParser:

    def __init__(self, sigData):
        self.roomId = sigData[commonDataTag.TAG_ROOMId]
        self.userId = sigData[commonDataTag.TAG_USERID]
        self.data = sigData[commonDataTag.TAG_DATA]

    def getRoomId(self):
        return self.roomId

    def getUserId(self):
        return self.userId

    def getData(self):
        return self.data


class sigServiceCore:

    def OnJoin(self, data):
        logUtils.info("OnJoin" + str(data))
        sigData = sigDataParser(data)
        # join room

        join_room(sigData.getRoomId())
        # send msg back
        socketService.send_to_self(commonDataTag.SING_JOINED, "server:join room successfully")

        # send msg to others in the room
        socketService.send_to_other(commonDataTag.SING_OTHER_JOINED, sigData.getRoomId(),
                                    "server: other joined: " + sigData.getUserId())

    def OnMessage(self, data):
        logUtils.info("message  transmit " + str(data))

        sigData = sigDataParser(data)

        socketService.send_to_other(commonDataTag.SING_MESSAGE, sigData.getRoomId(), sigData.getData())

    def OnLeave(self, data):
        logUtils.info("OnLeave" + str(data))
        sigData = sigDataParser(data)
        # leave room
        leave_room(sigData.getRoomId())
        # msg return
        socketService.send_to_self(commonDataTag.SING_LEAVED, "server:you have leaved successfully")
        # notify others
        socketService.send_to_other(commonDataTag.SING_OTHER_LEAVED,sigData.getRoomId(),"other has leaved...")
