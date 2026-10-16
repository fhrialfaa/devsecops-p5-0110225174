"""Validasi input pengguna."""
from datetime import date

VALID_PRIORITIES = ("low", "medium", "high")
MAX_TITLE_LEN = 100


def validate_title(title: str) -> str:
    title = (title or "").strip()
    if not title:
        raise ValueError("Judul tidak boleh kosong")
    if len(title) > MAX_TITLE_LEN:
        raise ValueError(f"Judul maksimal {MAX_TITLE_LEN} karakter")
    return title


def validate_priority(priority: str) -> str:
    priority = (priority or "").lower()
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Prioritas harus salah satu dari {VALID_PRIORITIES}")
    return priority


def validate_due(due: str) -> str:
    if not due:
        return ""
    try:
        date.fromisoformat(due)
    except ValueError as exc:
        raise ValueError("Format tanggal harus YYYY-MM-DD") from exc
    return due
