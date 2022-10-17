# whatsapp-api-webhook-server-python

[![Python application](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-publish.yml)

Python библиотека для интеграции с мессенджером WhatsAPP через API сервиса [green-api.com](https://green-api.com). Чтобы воспользоваться библиотекой нужно получить регистрационный токен и id аккаунта в [личном кабинете](https://console.green-api.com). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является оберткой к REST API, поэтому документация по ссылке выше применима и к самой библиотеке.

## Установка

```
pip install whatsapp-api-webhook-server-python
```

## Import 

```
import whatsapp_api_webhook_server_python.webhooksHandler as webhooksHandler
```

## Запуск сервера

```
webhooksHandler.startServer('127.0.0.1', 8000, onEvent)
```

onEvent - метод обработки вебхуков, который определяет разработчик.
В методе должно быть три параметра:
- webhooksHandler - экземляр класса библиотеки
- typeWebhook - тип вебхука
- body - тело сообщения

См. пример [echo.py](https://github.com/green-api/whatsapp-api-webhook-server-python/blob/master/examples/echo.py)
