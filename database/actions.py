import logging

from aiogram.types import User
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Person

logger = logging.getLogger(__name__)


async def add_user_to_db(session: AsyncSession, from_user: User):
    if not await session.get(Person, from_user.id):
        obj = Person(
            first_name=from_user.first_name,
            last_name=from_user.last_name,
            user_id=from_user.id
        )
        session.add(obj)
        await session.commit()
        logger.info('user with id %s added to db', from_user.id)