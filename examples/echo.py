from datetime import datetime
import json

import whatsapp_api_webhook_server_python.webhooksHandler as webhooksHandler


def onEvent(webhookHandler: webhooksHandler, typeWebhook: str, body):
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

def onIncomingMessageReceived(webhookHandler: webhooksHandler, body: object):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
        + 'At ' + str(eventDate) + ' Incoming from ' \
        + json.dumps(senderData, ensure_ascii=False) \
        + ' message = ' + json.dumps(messageData, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onIncomingCall(webhookHandler: webhooksHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    fromWho = body['from']
    TextOut = idMessage + ': ' \
        + 'Call from ' + fromWho \
        + ' at ' + str(eventDate)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onDeviceInfo(webhookHandler: webhooksHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    deviceData = body['deviceData']
    TextOut = 'At ' + str(eventDate) + ': ' \
        + json.dumps(deviceData, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onOutgoingMessageReceived(webhookHandler: webhooksHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
        + 'At ' + str(eventDate) + ' Outgoing from ' \
        + json.dumps(senderData, ensure_ascii=False) \
        + ' message = ' + json.dumps(messageData, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onOutgoingAPIMessageReceived(webhookHandler: webhooksHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    TextOut = idMessage + ': ' \
        + 'At ' + str(eventDate) + ' API outgoing from ' \
        + json.dumps(senderData, ensure_ascii=False) + \
        ' message = ' + json.dumps(messageData, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onOutgoingMessageStatus(webhookHandler: webhooksHandler, body):
    idMessage = body['idMessage']
    status = body['status']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    TextOut = idMessage + ': ' + str(eventDate) + ' status = ' + status
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onStateInstanceChanged(webhookHandler: webhooksHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    stateInstance = body['stateInstance']
    TextOut = 'At ' + str(eventDate) + ' state instance = ' \
        + json.dumps(stateInstance, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onStatusInstanceChanged(webhookHandler: webhooksHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    statusInstance = body['statusInstance']
    TextOut = 'At ' + str(eventDate) + ' status instance = ' \
        + json.dumps(statusInstance, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def main():
    webhooksHandler.startServer('127.0.0.1', 8000, onEvent)

if __name__ == "__main__":
    main()