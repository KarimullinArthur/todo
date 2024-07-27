from db import *

from formatter import *


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    create_task(name="English", content="English")
    oop = create_task(name="OOP", content="OOP")
    set_task_status(oop.id, True)

    tasks = get_tasks()
    for task in tasks:
        print(create_task_form(task))


if __name__ == "__main__":
    main()
