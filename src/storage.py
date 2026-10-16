"""Penyimpanan task ke file JSON."""
import json
import os
from .models import Task


class TaskStorage:
    def __init__(self, path: str = "tasks.json"):
        self.path = path

    def load(self) -> list[Task]:
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            return [Task(**item) for item in json.load(f)]

    def save(self, tasks: list[Task]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
