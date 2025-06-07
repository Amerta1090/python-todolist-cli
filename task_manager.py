# task_manager.py

from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def delete_task(self, task_id: int):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def mark_done(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "Selesai"
                return True
        return False

    def edit_task(self, task_id: int, **kwargs):
        for task in self.tasks:
            if task.id == task_id:
                task.title = kwargs.get("title", task.title)
                task.description = kwargs.get("description", task.description)
                task.priority = kwargs.get("priority", task.priority)
                task.deadline = kwargs.get("deadline", task.deadline)
                task.estimasi_waktu = kwargs.get("estimasi_waktu", task.estimasi_waktu)
                return True
        return False

    def get_task(self, task_id: int):
        return next((t for t in self.tasks if t.id == task_id), None)

    def list_tasks(self):
        return self.tasks

    def load_tasks(self, task_dicts: list):
        self.tasks = [Task.from_dict(td) for td in task_dicts]

    def to_dict_list(self):
        return [task.to_dict() for task in self.tasks]

    def generate_new_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1
    
    def filter_tasks(self, key, value):
        return [task for task in self.tasks if getattr(task, key).lower() == value.lower()]

    def search_tasks(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
