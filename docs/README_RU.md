# whatsapp-api-webhook-server-python

![](https://img.shields.io/badge/license-CC%20BY--ND%204.0-green)
![](https://img.shields.io/pypi/status/whatsapp-api-webhook-server-python)
![](https://img.shields.io/pypi/pyversions/whatsapp-api-webhook-server-python)
![](https://img.shields.io/github/actions/workflow/status/green-api/whatsapp-api-webhook-server-python/python-app.yml)
![](https://img.shields.io/pypi/dm/whatsapp-api-webhook-server-python)

whatsapp-api-webhook-server-python - библиотека для интеграции с мессенджером WhatsApp через API
сервиса [green-api.com](https://green-api.com/). Чтобы воспользоваться библиотекой, нужно получить регистрационный токен
и ID аккаунта в [личном кабинете](https://console.green-api.com/). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является оберткой к REST API,
поэтому документация по ссылке выше применима и к самой библиотеке.

## Авторизация

Чтобы отправить сообщение или выполнить другие методы Green API, аккаунт WhatsApp в приложении телефона должен быть в
авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://console.green-api.com/) и
сканируйте QR-код с использованием приложения WhatsApp.

## Примеры подготовки среды

### Пример подготовки среды для Ubuntu Server

#### Обновление системы

Обновим систему:

```shell
sudo apt update
sudo apt upgrade -y
```

#### Брандмауэр

Настроим брандмауэр:

Разрешим соединение по SSH:

```shell
sudo ufw allow ssh
```

Базовые правила:

```shell
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Разрешаем соединения по HTTP и HTTPS:

```shell
sudo ufw allow http
sudo ufw allow https
```

Активируем брандмауэр:

```shell
sudo ufw enable
```

#### Установка

Необходимо установить систему управления пакетами:

```shell
sudo apt install python3-pip
```

Установка библиотеки:

```shell
python3 -m pip install whatsapp-api-webhook-server-python
```

В качестве примера вы можете скачать и запустить [наш скрипт](../examples/echo.py). Скрипт отправляет в консоль все
входящие уведомления.

```shell
wget https://raw.githubusercontent.com/green-api/whatsapp-api-webhook-server-python/master/examples/echo.py
```

```shell
python3 -m echo.py
```

### Пример подготовки среды для Windows Server

#### Установка Python

На сервере должен быть установлен Python. [Инструкция по установке Python](https://www.python.org/downloads/).

#### Как настроить конфигурацию веб-сервера

Для использования IIS (Internet Information Services) в качестве веб-сервера требуется настроить файл
конфигурации `web.config`, чтобы служба IIS могла правильно выполнять код Python. Этот файл располагается в папке
публикации вашего веб-сервера.

После установки интерпретатора следует указать обработчик HttpPlatform в файле `web.config`. Этот обработчик будет
передавать подключения в автономный процесс Python.

Пример конфигурационного файла:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="PythonHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified"/>
        </handlers>
        <httpPlatform arguments="<Path-to-server-file>\echo.py"
                      processesPerApplication="16"
                      processPath="<Path-to-python>\python.exe"
                      startupTimeLimit="60"
                      stdoutLogEnabled="true"
                      stdoutLogFile="<Path-to-log-file>\python.log">
            <environmentVariables>
                <environmentVariable name="SOME_VARIABLE" value="%SOME_VAR%"/>
            </environmentVariables>
        </httpPlatform>
    </system.webServer>
</configuration>
```

- `<Path-to-python>` - путь к исполняемому файлу интерпретатора Python;
- `<Path-to-server-file>` - путь к исполняемому файлу сервера (например echo.py из примера);
- `<Path-to-log-file>` - путь к файлу логов.

Также потребуется открыть соответствующий порт во внешнюю сеть, установив настройки брандмауэра (дополнительные
параметры -> Правила для входящих подключений -> Создать правило -> Тип правила = Порт, Протоколы и порт -> TCP, указать
порт, Действие -> Разрешить соединение).

### Пример разворачивания среды сервера с использованием Docker

На машине должен быть установлен Docker.

Чтобы получить образ из Docker Hub, нужно написать команду:

```
sudo docker pull greenapi/whatsapp-api-webhook-server-python
```

Запустим образ в контейнере с указанием порта и отображением консоли:

```
sudo docker run --publish 8080:80 -it greenapi/whatsapp-api-webhook-server-python
```

Вместо порта 8080 можно указать любой свободный порт машины. В [личном кабинете](https://console.green-api.com/) нужно
будет указать IP (или внешнее имя машины) с указанием этого порта.

После запуска контейнера в консоль контейнера должны приходить входящие уведомления.

## Запуск сервера

Для использования в ваших решениях достаточно импортировать класс webhooksHandler.

```
import whatsapp_api_webhook_server_python.webhooksHandler as webhooksHandler
```

Старт сервера:

```
webhooksHandler.startServer('127.0.0.1', 80, onEvent)
```

Параметр `onEvent` - функция-обработчик, которую должен создать разработчик.

Параметры метода:

| Параметр        | Описание                    |
|-----------------|-----------------------------|
| webhooksHandler | экземпляр класса библиотеки |
| typeWebhook     | тип входящего уведомления   |
| body            | тело уведомления            |

Пример: [echo.py](../examples/echo.py).

## Как перенаправить входящие уведомления на веб-сервер

Чтобы перенаправить входящие уведомления, нужно в [личном кабинете](https://console.green-api.com/) установить адрес
отправки уведомлений (URL).

![](../media/ChangeWebhookServerURL.png)

## Документация по методам сервиса

[Документация по методам сервиса](https://green-api.com/docs/api/)

## Лицензия

Лицензировано на условиях [
Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)
](https://creativecommons.org/licenses/by-nd/4.0/). [LICENSE](../LICENSE).
