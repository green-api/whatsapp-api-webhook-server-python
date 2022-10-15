import json


class Webhooks():

    def webhookProccessing(dataText, onEvent):
        try:
            data = json.loads(dataText)
        except:
           return 
        body = data['body']
        typeWebhook = body['typeWebhook']
        onEvent(typeWebhook, body)