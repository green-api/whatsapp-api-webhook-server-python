import json


class Webhooks():

    def webhookProccessing(dataText, onEvent):
        try:
            data = json.loads(dataText)
        except:
           return 
        typeWebhook = data['typeWebhook']
        onEvent(typeWebhook, data)