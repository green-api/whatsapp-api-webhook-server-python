import requests
import whatsapp_api_webhook_server_python.webhooksHandler as webhooksHandler

result = None

class TestClass: 
    def test_getResponse(self):          
        webhooksHandler.startServer('127.0.0.1', 8000, onEvent)
        headers = {}
        payload = {
            'receiptId':1,
            'body':{'typeWebhook':'incomingMessageReceived'}}
        response = requests.request('POST', 'https://127.0.0.1:8000', 
            headers=headers, data=payload)
        if response.code != 200:
            print('Error code: ' + response.code)
        assert response.code == 200

def onEvent(webhooksHandler: webhooksHandler, typeWebhook: str, body):
    global result
    result = True

def main():
    TestClass.test_getResponse(TestClass)

if __name__ == "__main__":
    main()