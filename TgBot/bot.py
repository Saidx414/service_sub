import os
import telebot
from telebot import types
from sqlalchemy import create_engine, update, MetaData, Table
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

engine = create_engine(DB_URL)
metadata = MetaData()
users = Table("subscriptions_customuser", metadata, autoload_with=engine)

user_states = {}

@bot.message_handler(commands=["start"])
def handle_start(message):
    chat_id = message.chat.id
    user_states[chat_id] = "waiting_phone"
    bot.send_message(chat_id, "Привет! Пожалуйста, отправьте свой номер телефона:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text.strip()

    if user_states.get(chat_id) == "waiting_phone":
        phone = text

        with engine.connect() as conn:
            stmt = (
                update(users)
                .where(users.c.phone == phone)
                .values(telegram_id=chat_id)
            )
            result = conn.execute(stmt)
            conn.commit()

            if result.rowcount > 0:
                bot.send_message(chat_id, "Вы успешно зарегистрированы в системе!")
            else:
                bot.send_message(chat_id, "Пользователь с таким номером не найден.")

        user_states.pop(chat_id, None)
    else:
        bot.send_message(chat_id, "Пожалуйста, начните с команды /start.")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()

