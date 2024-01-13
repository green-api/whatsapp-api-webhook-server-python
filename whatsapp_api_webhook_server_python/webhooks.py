import json


class Webhooks():

    def webhookProccessing(dataText, onEvent):
        try:
            data = json.loads(dataText)
        except Exception as error:
            print(error)

            return
        typeWebhook = data['typeWebhook']
        onEvent(typeWebhook, data)
