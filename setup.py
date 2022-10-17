import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="whatsapp-api-webhook-server-python",
    version="0.0.4",
    install_requires=['tornado'],
    author="Ivan Sadovy",
    author_email="sadiv@bk.ru",
    description="This library helps you easily create a python '\
        'server application to get webhooks the WhatsApp API events '\
        'using service green-api.com",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/green-api/whatsapp-api-webhook-server-python",
    packages=['whatsapp_api_webhook_server_python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)