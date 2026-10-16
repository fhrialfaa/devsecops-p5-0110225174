"""CLI Task Manager. Contoh: python -m src.main add "Belajar DevSecOps" -p high"""
import argparse
from .service import TaskService
from .storage import TaskStorage


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Secure Task Manager")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Tambah task")
    add.add_argument("title")
    add.add_argument("-p", "--priority", default="medium")
    add.add_argument("-d", "--due", default="")

    sub.add_parser("list", help="Tampilkan semua task")

    done = sub.add_parser("done", help="Tandai task selesai")
    done.add_argument("id", type=int)

    rm = sub.add_parser("delete", help="Hapus task")
    rm.add_argument("id", type=int)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    service = TaskService(TaskStorage())
    try:
        if args.command == "add":
            t = service.add(args.title, args.priority, args.due)
            print(f"Ditambahkan: #{t.id} {t.title}")
        elif args.command == "list":
            for t in service.list():
                mark = "x" if t.done else " "
                print(f"[{mark}] #{t.id} {t.title} ({t.priority}) {t.due}")
        elif args.command == "done":
            service.complete(args.id)
            print("Task selesai")
        elif args.command == "delete":
            service.delete(args.id)
            print("Task dihapus")
    except (ValueError, KeyError) as err:
        print(f"Error: {err}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
