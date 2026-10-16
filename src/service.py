"""Logika bisnis Task Manager."""
from .models import Task
from .storage import TaskStorage
from .validators import validate_title, validate_priority, validate_due


class TaskService:
    def __init__(self, storage: TaskStorage):
        self.storage = storage

    def add(self, title: str, priority: str = "medium", due: str = "") -> Task:
        tasks = self.storage.load()
        new_id = max((t.id for t in tasks), default=0) + 1
        task = Task(new_id, validate_title(title),
                    validate_priority(priority), validate_due(due))
        tasks.append(task)
        self.storage.save(tasks)
        return task

    def complete(self, task_id: int) -> Task:
        tasks = self.storage.load()
        for t in tasks:
            if t.id == task_id:
                t.done = True
                self.storage.save(tasks)
                return t
        raise KeyError(f"Task {task_id} tidak ditemukan")

    def delete(self, task_id: int) -> None:
        tasks = self.storage.load()
        remaining = [t for t in tasks if t.id != task_id]
        if len(remaining) == len(tasks):
            raise KeyError(f"Task {task_id} tidak ditemukan")
        self.storage.save(remaining)

    def list(self, only_pending: bool = False) -> list[Task]:
        tasks = self.storage.load()
        return [t for t in tasks if not t.done] if only_pending else tasks
