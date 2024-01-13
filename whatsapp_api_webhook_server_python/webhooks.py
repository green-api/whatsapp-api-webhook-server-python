from json import JSONDecodeError, loads
from typing import Any, Callable, Optional


def handle_notification(
        notification: Optional[bytes],
        notification_handler: Callable[[str, dict], Any]
) -> None:
    try:
        data = loads(notification)
    except JSONDecodeError:
        return None

    webhook_type = data["typeWebhook"]

    notification_handler(webhook_type, data)
