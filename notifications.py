<<<<<<< HEAD
import requests                    # Для отправки HTTP-запросов к Telegram API
from config import TELEGRAM_TOKEN, CHAT_ID     # Импорт токена и chat_id из конфигурации

def send_to_telegram(message: str, chat_id=CHAT_ID):
    """Отправка сообщения в Telegram по API."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"   # Формируем url для Telegram API
    data = {"chat_id": chat_id, "text": message}                        # Формируем данные для отправки
    requests.post(url, data=data)                                       # Отправляем POST-запрос
=======
import requests                    # Для отправки HTTP-запросов к Telegram API
from config import TELEGRAM_TOKEN, CHAT_ID     # Импорт токена и chat_id из конфигурации

def send_to_telegram(message: str, chat_id=CHAT_ID):
    """Отправка сообщения в Telegram по API."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"   # Формируем url для Telegram API
    data = {"chat_id": chat_id, "text": message}                        # Формируем данные для отправки
    requests.post(url, data=data)                                       # Отправляем POST-запрос
>>>>>>> 2c61133ba2a13db18adcd184084f73e370918660
