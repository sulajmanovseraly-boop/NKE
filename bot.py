import os
import time
import csv
import telegram
from datetime import datetime

# Токен твоего Telegram бота
TOKEN = os.getenv("TOKEN")
bot = telegram.Bot(token=TOKEN)

# Путь к CSV
FILE_PATH = "feedback.csv"

last_update_id = None

def save_message(msg):
    with open(FILE_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg])
    print(f"Saved: {msg}")

while True:
    try:
        updates = bot.get_updates(offset=last_update_id, timeout=10)
        for update in updates:
            if update.message and update.message.text:
                msg = update.message.text
                chat_id = update.message.chat.id
                save_message(msg)
                bot.send_message(chat_id, "✅ Спасибо! Твоё сообщение сохранено анонимно.")
                last_update_id = update.update_id + 1
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
