from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args_ = (
        UniqueConstraint("foo", "bar"),  # значение двух столбцов составляют уникальное значение
    )

