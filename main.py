from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
    # тут мы принимаем юзера в канал
    await update.approve()
    # а тут отправляем сообщение
    await bot.send_message(chat_id=update.from_user.id, text="текст сообщения бота в лс юзеру")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)