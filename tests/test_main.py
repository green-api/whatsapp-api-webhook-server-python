import whatsapp_api_webhook_server_python.webhooksHandler as handler

result = None

class TestClass: 
    def test_Started(self):       
        started = True   
        try: 
            handler.startServer('127.0.0.1', 8000, onEvent, False)
        except:
            started = False
        assert started == True

def onEvent(webhooksHandler: handler.WebhooksHandler, typeWebhook: str, body):
    pass

def main():
    TestClass.test_Started(TestClass)

if __name__ == "__main__":
    main()