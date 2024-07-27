from datetime import datetime, UTC
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(default=datetime.now(UTC))]


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    name: Mapped[str]
    content: Mapped[str]
    is_done: Mapped[bool] = mapped_column(default=False)
    priority: Mapped[int | None]
    created_at: Mapped[created_at]

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} content={self.content} is_done={self.is_done} created_at={self.created_at}>"
