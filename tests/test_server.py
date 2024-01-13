import unittest

from whatsapp_api_webhook_server_python.webhooksHandler import startServer


class ServerTestCase(unittest.TestCase):
    def test_server(self):
        self.assertIsNone(startServer("127.0.0.1", 5000, None, False))


if __name__ == '__main__':
    unittest.main()
