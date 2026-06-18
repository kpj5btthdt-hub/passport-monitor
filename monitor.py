import requests

BOT_TOKEN = "7916276976: AAFWIZ6xheSTdeBsWp4Ld
Qy9VkKs62KfXzI"
CHAT_ID = "1616149951"

URL = "https://munich.pasport.org.ua/solutions/e-queue"

response = requests.get(URL)
text = response.text

if "Усі місця зайняті" not in text and "Все места заняты" not in text:
    message = "⚠️ Возможно, появились свободные места!\nhttps://munich.pasport.org.ua/solutions/e-queue"
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": message}
    )
