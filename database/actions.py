from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


async def add_user(session: AsyncSession, name: str):
    obj = User(
        name=name,
    )
    session.add(obj)
    await session.commit()