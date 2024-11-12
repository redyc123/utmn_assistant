import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os
from api import chatting

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ["TG_BOT"])
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я ассистент студента ТюмГУ")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Я могу отвечать на любые текстовые сообщения.")


@dp.message()
async def echo_message(msg: types.Message):
    message = ""
    async for t in chatting([{"role": "user", "content": msg.text}]):
        message += t
    await bot.send_message(msg.from_user.id, message)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
