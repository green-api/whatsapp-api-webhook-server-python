# whatsapp-api-webhook-server-python

![](https://img.shields.io/badge/license-CC%20BY--ND%204.0-green)
![](https://img.shields.io/pypi/status/whatsapp-api-webhook-server-python)
![](https://img.shields.io/pypi/pyversions/whatsapp-api-webhook-server-python)
![](https://img.shields.io/github/actions/workflow/status/green-api/whatsapp-api-webhook-server-python/python-package.yml)
![](https://img.shields.io/pypi/dm/whatsapp-api-webhook-server-python)

## Support links

[![Support](https://img.shields.io/badge/support@green--api.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@greenapi.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_eng_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/77273122366)

## Guides & News

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@greenapi-en)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaLj6J4LNSa2B5Jx6s3h)

- [Документация на русском языке](https://github.com/green-api/whatsapp-api-webhook-server-python/blob/master/docs/README_RU.md).

whatsapp-api-webhook-server-python is a library for integration with WhatsApp messenger using the API
service [green-api.com](https://green-api.com/en/). You should get a registration token and an account ID in
your [personal cabinet](https://console.green-api.com/) to use the library. There is a free developer account tariff.

## API

The documentation for the REST API can be found at the [link](https://green-api.com/en/docs/). The library is a wrapper
for the REST API, so the documentation at the link above also applies.

## Authorization

To send a message or perform other Green API methods, the WhatsApp account in the phone app must be authorized. To
authorize the account, go to your [cabinet](https://console.green-api.com/) and scan the QR code using the WhatsApp app.

## Examples of preparing the environment

### Example of preparing the environment for Ubuntu Server

#### Updating the system

Update the system:

```shell
sudo apt update
sudo apt upgrade -y
```

#### Firewall

Set up the firewall:

Allow the SSH connection:

```shell
sudo ufw allow ssh
```

Base rules:

```shell
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Allow HTTP and HTTPS connections:

```shell
sudo ufw allow http
sudo ufw allow https
```

Enable the firewall:

```shell
sudo ufw enable
```

#### Installation

A package management system must be installed:

```shell
sudo apt install python3-pip
```

Library installation:

```shell
python3 -m pip install whatsapp-api-webhook-server-python
```

As an example you can download and run [our script](
https://github.com/green-api/whatsapp-api-webhook-server-python/blob/master/examples/echo.py
). The script sends all incoming notifications.

```shell
wget https://raw.githubusercontent.com/green-api/whatsapp-api-webhook-server-python/master/examples/echo.py
```

```shell
python3 -m echo.py
```

### Example of preparing the environment for Windows Server

#### Python installation

Python must be installed on the server. [Python installation instructions](https://www.python.org/downloads/).

#### Как настроить конфигурацию веб-сервера

To use IIS (Internet Information Services) as a web server, you need to configure the configuration file `web.config` so
that the IIS service can properly execute Python code. This file is located in the publication folder of your web
server.

After installing the interpreter, you should define the HttpPlatform handler in the `web.config` file. This handler will
transfer connections to the standalone Python process.

Example configuration file:

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

- `<Path-to-python>` - the path to the executable file of the Python interpreter;
- `<Path-to-server-file>` - the path to the server executable file (e.g. echo.py from the example);
- `<Path-to-log-file>` - the path to the log file.

You will also need to open the corresponding port to the external network by setting the firewall settings (Advanced
Options -> Rules for incoming connections -> Create Rule -> Rule Type = Port Protocols, Port -> TCP, specify the
firewall settings. options -> Rules for incoming connections -> Create Rule -> Rule Type = Port, Protocols and Port ->
TCP, specify port, Action -> Allow connection).

### An example of deploying a server environment using Docker

The machine should have Docker installed.

To get an image from the Docker Hub, you need to write a command:

```
sudo docker pull greenapi/whatsapp-api-webhook-server-python
```

Run the image in a container with the port and the console displayed:

```
sudo docker run --publish 8080:80 -it greenapi/whatsapp-api-webhook-server-python
```

You can specify any free machine port instead of port 8080. In [personal cabinet](https://console.green-api.com/) you
will need to specify the IP (or external machine name) with this port.

After starting the container, the container console should receive incoming notifications.

## Running the server

To use in your solutions, simply import the webhooksHandler class.

```
import whatsapp_api_webhook_server_python.webhooksHandler as webhooksHandler
```

Start of the server:

```
webhooksHandler.startServer('127.0.0.1', 80, onEvent)
```

The `onEvent` parameter is a handler function that should be created by the developer.

Method parameters:

| Parameter       | Description                   |
|-----------------|-------------------------------|
| webhooksHandler | library class instance        |
| typeWebhook     | type of incoming notification |
| body            | notification body             |

Example: [echo.py](https://github.com/green-api/whatsapp-api-webhook-server-python/blob/master/examples/echo.py).

## How to reroute incoming notifications to a web server

To reroute incoming notifications, you need to set the notification sending address (URL)
in [personal cabinet](https://console.green-api.com/).

## Service methods documentation

[Service methods documentation](https://green-api.com/en/docs/api/)

## License

Licensed under [
Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)
](https://creativecommons.org/licenses/by-nd/4.0/) terms.
Please see file [LICENSE](https://github.com/green-api/whatsapp-api-webhook-server-python/blob/master/LICENSE).
