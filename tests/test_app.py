import os
import tempfile
import unittest
from datetime import date

from src.models import Task
from src.service import TaskService
from src.storage import TaskStorage
from src.validators import validate_title, validate_priority, validate_due


class TestValidators(unittest.TestCase):
    def test_title_empty(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_priority_invalid(self):
        with self.assertRaises(ValueError):
            validate_priority("urgent")

    def test_due_invalid(self):
        with self.assertRaises(ValueError):
            validate_due("31-12-2026")


class TestModel(unittest.TestCase):
    def test_overdue(self):
        t = Task(1, "x", due="2020-01-01")
        self.assertTrue(t.is_overdue(date(2026, 1, 1)))
        t.done = True
        self.assertFalse(t.is_overdue(date(2026, 1, 1)))


class TestService(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.path)
        self.service = TaskService(TaskStorage(self.path))

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_complete_delete(self):
        t = self.service.add("Belajar CI/CD", "high", "2026-12-31")
        self.assertEqual(t.id, 1)
        self.service.complete(1)
        self.assertEqual(self.service.list(only_pending=True), [])
        self.service.delete(1)
        self.assertEqual(self.service.list(), [])

    def test_missing_task(self):
        with self.assertRaises(KeyError):
            self.service.complete(99)


if __name__ == "__main__":
    unittest.main()
