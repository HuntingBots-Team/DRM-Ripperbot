class TaskSession:
    def __init__(self):
        self.format = None  # 'mp4' or 'mkv'
        self.destination = None  # 'gdrive' or 'telegram'

user_tasks = {}

def get_task(user_id):
    if user_id not in user_tasks:
        user_tasks[user_id] = TaskSession()
    return user_tasks[user_id]

def reset_task(user_id):
    if user_id in user_tasks:
        del user_tasks[user_id]  # Task manager logic placeholder
