from datetime import datetime
from io import BytesIO, TextIOBase
import json

import whatsapp_api_webhook_server_python.webhooksHTTPRequestHandler as webhooksHTTPRequestHandler
from whatsapp_api_webhook_server_python.webhooks import TypeWebhook as TypeWebhook

def onEvent(webhookHandler: webhooksHTTPRequestHandler, typeWebhook: str, body):
    if typeWebhook == TypeWebhook.INCOMING_MESSAGE_RECEIVED.value:
        onIncomingMessageReceived(webhookHandler, body)      
    elif typeWebhook == TypeWebhook.DEVICE_INFO.value:   
        onDeviceInfo(webhookHandler, body)              
    elif typeWebhook == TypeWebhook.INCOMING_CALL.value:
        onIncomingCall(webhookHandler, body)
    elif typeWebhook == TypeWebhook.INCOMING_MESSAGE_RECEIVED.value:
        onIncomingMessageReceived(webhookHandler, body)
    elif typeWebhook == TypeWebhook.OUTGOING_API_MESSAGE_RECEIVED.value:
        onOutgoingAPIMessageReceived(webhookHandler, body)
    elif typeWebhook == TypeWebhook.OUTGOING_MESSAGE_RECEIVED.value:
        onOutgoingMessageReceived(webhookHandler, body)
    elif typeWebhook == TypeWebhook.OUTGOING_MESSAGE_STATUS.value:
        onOutgoingMessageStatus(webhookHandler, body)
    elif typeWebhook == TypeWebhook.STATE_INSTANCE_CHANGED.value:
        onStateInstanceChanged(webhookHandler, body)
    elif typeWebhook == TypeWebhook.STATUS_INSTANCE_CHANGED.value:
        onStatusInstanceChanged(webhookHandler, body)

def onIncomingMessageReceived(webhookHandler: webhooksHTTPRequestHandler, body: object):
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

def onIncomingCall(webhookHandler: webhooksHTTPRequestHandler, body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    fromWho = body['from']
    TextOut = idMessage + ': ' \
        + 'Call from ' + fromWho \
        + ' at ' + str(eventDate)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onDeviceInfo(webhookHandler: webhooksHTTPRequestHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    deviceData = body['deviceData']
    TextOut = 'At ' + str(eventDate) + ': ' \
        + json.dumps(deviceData, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onOutgoingMessageReceived(webhookHandler: webhooksHTTPRequestHandler, body):
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

def onOutgoingAPIMessageReceived(webhookHandler: webhooksHTTPRequestHandler, body):
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

def onOutgoingMessageStatus(webhookHandler: webhooksHTTPRequestHandler, body):
    idMessage = body['idMessage']
    status = body['status']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    TextOut = idMessage + ': ' + str(eventDate) + ' status = ' + status
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onStateInstanceChanged(webhookHandler: webhooksHTTPRequestHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    stateInstance = body['stateInstance']
    TextOut = 'At ' + str(eventDate) + ' state instance = ' \
        + json.dumps(stateInstance, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def onStatusInstanceChanged(webhookHandler: webhooksHTTPRequestHandler, body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    statusInstance = body['statusInstance']
    TextOut = 'At ' + str(eventDate) + ' status instance = ' \
        + json.dumps(statusInstance, ensure_ascii=False)
    webhookHandler.wfile.write((50 * '-' + '\n').encode("utf-8"))
    webhookHandler.wfile.write(TextOut.encode("utf-8"))

def main():
    webhooksHTTPRequestHandler.startServer('127.0.0.1', 8000, onEvent)

if __name__ == "__main__":
    main()