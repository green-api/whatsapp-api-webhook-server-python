import json
from ast import literal_eval
from enum import Enum


class TypeWebhook(Enum):
    INCOMING_MESSAGE_RECEIVED = 'incomingMessageReceived'
    OUTGOING_MESSAGE_RECEIVED = 'outgoingMessageReceived'
    OUTGOING_API_MESSAGE_RECEIVED = 'outgoingAPIMessageReceived'
    OUTGOING_MESSAGE_STATUS  = 'outgoingMessageStatus'
    STATE_INSTANCE_CHANGED  = 'stateInstanceChanged'
    STATUS_INSTANCE_CHANGED  = 'statusInstanceChanged'
    DEVICE_INFO  = 'deviceInfo'
    INCOMING_CALL  = 'incomingCall'

class Webhooks():

    def webhookProccessing(dataText, onEvent):
        try:
            data = json.loads(dataText)
        except:
           return 
        body = data['body']
        typeWebhook = body['typeWebhook']
        onEvent(typeWebhook, body)