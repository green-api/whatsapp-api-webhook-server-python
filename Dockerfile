FROM ubuntu
LABEL maintainer="Green API <support@green-api.com>"

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    wget \
    curl

# Working directory
WORKDIR /webhook-server

# Install library
RUN pip3 install whatsapp-api-webhook-server-python
# Download example
RUN wget https://raw.githubusercontent.com/green-api/whatsapp-api-webhook-server-python/master/examples/echo.py
# Start server
CMD [ "python3","-u","./echo.py" ]