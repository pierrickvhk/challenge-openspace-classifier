import argparse
from typing import List

from utils.file_utils import read_names_from_txt
from utils.openspace import OpenSpace
from utils.table import Table


def build_default_openspace() -> OpenSpace:
    """Create the default room: 6 tables x 4 seats = 24 seats."""
    tables = [Table(4, f"Table {i+1}") for i in range(6)]
    return OpenSpace(tables)


def run(file_path: str, seed: int | None, save: bool) -> int:
    """
    Load names, organize seats, display results, optionally save CSV.

    :param file_path: path to .txt file with names
    :param seed: optional random seed for reproducible results
    :param save: if True, save CSV as openspace.csv
    :return: exit code (0 OK, 1 overflow)
    """
    names: List[str] = read_names_from_txt(file_path)
    space = build_default_openspace()
    placed, overflow = space.organize(names, seed=seed)

    space.display()
    if overflow > 0:
        print(f"\n⚠️Overflow⚠️: {overflow} person(s) could not be seated.")
    else:
        print("\n✅ Everyone has a seat. ✅")

    if save:
        space.store("openspace.csv")

    return 0 if overflow == 0 else 1


def parse_args() -> argparse.Namespace:
    """Parse command line options."""
    p = argparse.ArgumentParser(description="Open Space Organizer")
    p.add_argument("file", help="Path to .txt file with names (one per line)")
    p.add_argument("--seed", type=int, default=None, help="Optional random seed")
    p.add_argument("--save", action="store_true", help="Save the assignment to openspace.csv")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    raise SystemExit(run(args.file, args.seed, args.save))
