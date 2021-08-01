from flask_socketio import join_room, leave_room

from commonUtils.dataFlags import commonDataTag
from commonUtils.logManager import logUtils
from sigSys.socketMsgUtilsr import socketService



class sigDataParser:

    def __init__(self, sigData):
        if sigData.keys().__contains__(commonDataTag.TAG_USERID):
            self.userId = sigData[commonDataTag.TAG_USERID]
        else:
            self.userId=0
        if sigData.keys().__contains__(commonDataTag.TAG_DATA):
            self.data = sigData[commonDataTag.TAG_DATA]
        else:
            self.data={}

    def getUserId(self):
        return self.userId

    def getData(self):

        return self.data


class sigServiceCore:

    def OnJoin(self, roomId,data):
        logUtils.info("OnJoin" + str(data))
        # join room

        join_room(roomId)
        # send msg back
        socketService.send_to_self(commonDataTag.SING_JOINED,roomId,"server:u hava joined the rooom")

        # send msg to others in the room
        socketService.send_to_other(commonDataTag.SING_OTHER_JOINED,roomId,
                                    "server: other joined: ")

    def OnMessage(self,roomId,data):
        logUtils.info("message  transmit " + str(data))

        socketService.send_to_other(commonDataTag.SING_MESSAGE, roomId, data)

    def OnLeave(self, roomid,data):
        logUtils.info("OnLeave" + str(data))
        # leave room
        leave_room(roomid)
        # msg return
        socketService.send_to_self(commonDataTag.SING_LEAVED,roomid,"server:you have leaved successfully")
        # notify others
        socketService.send_to_other(commonDataTag.SING_OTHER_LEAVED,roomid,"other has leaved...")
