from sqlalchemy import DateTime, Float, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass
    # created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    # updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    # description: Mapped[str] = mapped_column(Text)
    # price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    # image: Mapped[str] = mapped_column(String(150))