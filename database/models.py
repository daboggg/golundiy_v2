from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass
    # created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    # updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Person(Base):
    __tablename__ = 'users'

    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=True)
    last_name: Mapped[str] = mapped_column(String(20), nullable=True)

    is_active: Mapped[bool] = mapped_column(default=False)

    msg_received: Mapped[int] = mapped_column(default=0)

    is_privileged: Mapped[bool] = mapped_column(default=False)