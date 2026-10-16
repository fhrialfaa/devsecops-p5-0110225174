"""Model data untuk aplikasi Task Manager."""
from dataclasses import dataclass, asdict
from datetime import date


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    due: str = ""
    done: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    def is_overdue(self, today: date | None = None) -> bool:
        if self.done or not self.due:
            return False
        today = today or date.today()
        return date.fromisoformat(self.due) < today
