from datetime import datetime
import json

import whatsapp_api_webhook_server_python.webhooksHandler as handler


def onEvent(webhookHandler: handler.WebhooksHandler, typeWebhook: str, body):
    if typeWebhook == 'incomingMessageReceived':
        onIncomingMessageReceived(webhookHandler, body)      
    elif typeWebhook == 'deviceInfo':   
        onDeviceInfo(webhookHandler, body)              
    elif typeWebhook == 'incomingCall':
        onIncomingCall(webhookHandler, body)
    elif typeWebhook == 'incomingMessageReceived':
        onIncomingMessageReceived(webhookHandler, body)
    elif typeWebhook == 'outgoingAPIMessageReceived':
        onOutgoingAPIMessageReceived(webhookHandler, body)
    elif typeWebhook == 'outgoingMessageReceived':
        onOutgoingMessageReceived(webhookHandler, body)
    elif typeWebhook == 'outgoingMessageStatus':
        onOutgoingMessageStatus(webhookHandler, body)
    elif typeWebhook == 'stateInstanceChanged':
        onStateInstanceChanged(webhookHandler, body)
    elif typeWebhook == 'statusInstanceChanged':
        onStatusInstanceChanged(webhookHandler, body)

def onIncomingMessageReceived(webhookHandler: handler.WebhooksHandler, body: object):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
        + 'At ' + str(eventDate) + ' Incoming from ' \
        + json.dumps(senderData, ensure_ascii=False) \
        + ' message = ' + json.dumps(messageData, ensure_ascii=False)
    webhookHandler.set_status(200)
    print(TextOut)

def onIncomingCall(webhookHandler: handler.WebhooksHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    fromWho = body['from']
    TextOut = idMessage + ': ' \
        + 'Call from ' + fromWho \
        + ' at ' + str(eventDate)
    webhookHandler.set_status(200)
    print(TextOut)

def onDeviceInfo(webhookHandler: handler.WebhooksHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    deviceData = body['deviceData']
    TextOut = 'At ' + str(eventDate) + ': ' \
        + json.dumps(deviceData, ensure_ascii=False)
    webhookHandler.set_status(200)
    print(TextOut)

def onOutgoingMessageReceived(webhookHandler: handler.WebhooksHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
        + 'At ' + str(eventDate) + ' Outgoing from ' \
        + json.dumps(senderData, ensure_ascii=False) \
        + ' message = ' + json.dumps(messageData, ensure_ascii=False)
    webhookHandler.set_status(200)
    print(TextOut)

def onOutgoingAPIMessageReceived(webhookHandler: handler.WebhooksHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
        + 'At ' + str(eventDate) + ' API outgoing from ' \
        + json.dumps(senderData, ensure_ascii=False) + \
        ' message = ' + json.dumps(messageData, ensure_ascii=False)
    webhookHandler.set_status(200)
    print(TextOut)

def onOutgoingMessageStatus(webhookHandler: handler.WebhooksHandler, body):
    idMessage = body['idMessage']
    status = body['status']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    TextOut = idMessage + ': ' + str(eventDate) + ' status = ' + status
    webhookHandler.set_status(200)
    print(TextOut)

def onStateInstanceChanged(webhookHandler: handler.WebhooksHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    stateInstance = body['stateInstance']
    TextOut = 'At ' + str(eventDate) + ' state instance = ' \
        + json.dumps(stateInstance, ensure_ascii=False)
    webhookHandler.set_status(200)
    print(TextOut)

def onStatusInstanceChanged(webhookHandler: handler.WebhooksHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    statusInstance = body['statusInstance']
    TextOut = 'At ' + str(eventDate) + ' status instance = ' \
        + json.dumps(statusInstance, ensure_ascii=False)
    webhookHandler.set_status(200)
    print(TextOut)

def main():
    handler.startServer('127.0.0.1', 8000, onEvent)

if __name__ == "__main__":
    main()