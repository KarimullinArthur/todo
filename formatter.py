def create_task_form(task, id=False) -> str:
    if task.is_done:
        status = "✅"
    else:
        status = "▢"

    if id:
        id = str(task.id) + ' '
    else:
        id = ''

    return f"""{id}* {task.name} {status}"""
