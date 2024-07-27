def create_task_form(task) -> str:
    if task.is_done:
        status = "✅"
    else:
        status = "▢"

    return f"""* {task.name} {status}"""

