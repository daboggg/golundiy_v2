from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.schedulers.asyncio import AsyncIOScheduler

from settings import settings

bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage())
# scheduler = AsyncIOScheduler(timezone="Europe/Moscow", jobstores={'sqlalchemy': SQLAlchemyJobStore(url=settings.db.db_url)})
# scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
# scheduler.add_jobstore('sqlalchemy', url=settings.db.db_url)