from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import engine
from .models import Task


session = Session(engine)


def get_task(task_id: int | str) -> Task:
    with session:
        result = session.scalars(select(Task).where(Task.id == task_id)).one()
        assert result is not None
        return result


def get_tasks():
    with session:
        result = session.scalars(select(Task)).all()
        assert result is not None
        return result


def create_task(name: str, content: str | None = None) -> Task:
    with session:
        task = Task(name=name, content=content)

        session.add(task)
        session.commit()

        return session.scalars(select(Task).where(Task.id == task.id)).one()


def set_task_status(task_id: int | str, done: bool) -> None:
    with session:
        task = get_task(task_id)
        assert task is not None
        task.is_done = done
        session.add(task)
        session.commit()


def del_task(task_id: int | str) -> None:
    with session:
        task = get_task(task_id)
        session.delete(task)
