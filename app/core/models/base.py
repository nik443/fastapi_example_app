from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from app.utils.case_converter import camel_to_snake_case
from app.core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_to_snake_case(cls.__name__)}s"

    id: Mapped[int] = mapped_column(primary_key=True)


