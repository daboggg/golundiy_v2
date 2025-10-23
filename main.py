import asyncio
import logging

from aiogram import Bot

from bot.core import dp, bot
from bot.handlers.cmd import cmd_router
from database.engine import create_db, drop_db, session_maker
from middlewares.db import DataBaseSession
from settings import settings


async def start_bot():
    # await drop_db()
    await create_db()
    # await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot():
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')
    # scheduler.shutdown()


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'

                        )
    logger = logging.getLogger(__name__)

    # запускаю скедулер
    # scheduler.start()


    # регистрация middlewares
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    # dp.update.middleware.register(SchedulerMiddleware(scheduler))

    # подключение роутеров
    dp.include_routers(
        # main,
        cmd_router,
        # main_dialog,
        # list_subscriptions_dialog,
        # admin_dialog,
    )

    # подключение диалогов
    # setup_dialogs(dp)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)



    logger.info("Бот запущен!")

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
