# whatsapp-api-webhook-server-python

[![Python application](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/green-api/whatsapp-api-webhook-server-python/actions/workflows/python-publish.yml)

Python библиотека для интеграции с мессенджером WhatsAPP через API сервиса [green-api.com](https://green-api.com). Чтобы воспользоваться библиотекой нужно получить регистрационный токен и id аккаунта в [личном кабинете](https://console.green-api.com). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является оберткой к REST API, поэтому документация по ссылке выше применима и к самой библиотеке.

## Подготовка среды

На машине должен быть установлен Python 3 последней версии, который можно скачать 
с официального сайта: [python.org](https://www.python.org/downloads/)

## Пример подготовки среды сервера на операционной системе Ubuntu

После создания машины для сервера нужно настроить на ней брандмауэр, установить необходимые компоненты и запустить сервер.

Ubuntu 20.04 и выше поставляются с предустановленным Python 3.
Обновим систему:
```
sudo apt update
sudo apt -y upgrade
```

Нужно настроить правила брандмауэра. В Ubuntu брандмауэр UFW установлен по умолчанию, но если по какой-то причине он не установлен, установим:
```
sudo apt install ufw
```

Сначала создадим правила брандмауэра по-умолчанию:
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Если мы сейчас активируем брандмауэр UFW, все входящие соединения будут запрещены.
Чтобы после активации бранмауэра нам было доступно соединение по SSH нужно добавить правила:
```
sudo ufw allow ssh
```

Соединения HTTP на порту 80, которые используются веб-серверами без шифрования, с помощью команды:
```
sudo ufw allow http
```

Соединения HTTPS на порту 443, которые используются веб-серверами с шифрованием, с помощью команды: 
```
sudo ufw allow https
```

Если на вашем сервере имеется публичный сетевой интерфейс под названием eth0, вы можете разрешить трафик HTTP (порт 80) для этого интерфейса с помощью следующей команды:
```
sudo ufw allow in on eth0 to any port 80
```

Название сетевого интерфейса можно узнать с помощью команды:
```
ip addr
```

Активация брандмауэра UFW:
```
sudo ufw enable
```

Теперь наш сервер может принимать входящие запросы на указанный нами порт.

Установим систему управления пакетами pip, если он не содержиться в дистрибутиве ОС:
```
sudo apt install -y python3-pip
```

Теперь можно устанавливать нашу библиотеку.

Установка библиотеки:
```
pip3 install whatsapp-api-webhook-server-python
```

Можно в качестве примера запустить на сервере наш скрипт echo.py, он будет выводить в консоль информацию о полученных вэбхуках:
```
wget https://raw.githubusercontent.com/green-api/whatsapp-api-webhook-server-python/master/examples/echo.py
python3 echo.py
```

## Запуск сервера

Для использования в ваших решениях достаточно импортировать класс webhooksHandler
```
import whatsapp_api_webhook_server_python.webhooksHandler as webhooksHandler
```

Старт сервера:
```
webhooksHandler.startServer('127.0.0.1', 80, onEvent)
```

onEvent - метод обработки вебхуков, который определяет разработчик.
В методе должно быть три параметра:
- webhooksHandler - экземляр класса библиотеки
- typeWebhook - тип вебхука
- body - тело сообщения

См. пример [echo.py](https://github.com/green-api/whatsapp-api-webhook-server-python/blob/master/examples/echo.py)
