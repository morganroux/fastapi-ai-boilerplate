from abc import ABC, abstractmethod
from typing import Dict, Any

class MessageProviderInterface(ABC):
    @abstractmethod
    def send_message(self, recipient: str, title: str, message: str, message_type: str) -> Dict[str, Any]:
        pass

class EmailProvider(MessageProviderInterface):
    def send_message(self, recipient: str, title: str, message: str, message_type: str) -> Dict[str, Any]:
        # Email sending implementation would go here
        # For now, we'll return a success response
        return {
            "success": True,
            "provider": "email",
            "recipient": recipient,
            "message_id": f"email_{hash(recipient + title + message)}"
        }

class SMSProvider(MessageProviderInterface):
    def send_message(self, recipient: str, title: str, message: str, message_type: str) -> Dict[str, Any]:
        # SMS sending implementation would go here
        # For now, we'll return a success response
        return {
            "success": True,
            "provider": "sms",
            "recipient": recipient,
            "message_id": f"sms_{hash(recipient + title + message)}"
        }

class ConsoleProvider(MessageProviderInterface):
    def send_message(self, recipient: str, title: str, message: str, message_type: str) -> Dict[str, Any]:
        print(f"[{message_type.upper()}] To: {recipient}")
        print(f"Title: {title}")
        print(f"Message: {message}")
        print("-" * 50)
        return {
            "success": True,
            "provider": "console",
            "recipient": recipient,
            "message_id": f"console_{hash(recipient + title + message)}"
        }