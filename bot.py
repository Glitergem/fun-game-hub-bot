import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
import os

# --- CONFIGURATION ---
TOKEN = os.getenv("BOT_TOKEN")  # Render will store your token securely

# --- SETUP ---
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# --- START COMMAND ---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = (
        "👋 សួស្តី! ស្វាគមន៍មកកាន់ **Fun Game Hub** 🎮\n"
        "នៅទីនេះអ្នកអាចសាកល្បងហ្គេមសប្បាយៗ និងស្វែងយល់អំពីបូតថ្មីៗ។\n\n"
        "👋 Welcome to **Fun Game Hub!** 🎮\n"
        "Discover fun mini-games and explore new Telegram bots every day.\n\n"
        "👉 ចុចខាងក្រោមដើម្បីចូលទៅកាន់បូតចម្បង៖"
    )

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="👉 Visit Main Bot 🎯",
            url="https://t.me/faxkh888888888bot"
        )
    )

    await message.answer(text, parse_mode="Markdown", reply_markup=keyboard)

# --- RUN BOT ---
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
