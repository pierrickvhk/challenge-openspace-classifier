import csv
import random
from pathlib import Path
from typing import Iterable, List, Tuple

from utils.table import Table


class OpenSpace:
    """Class that manages tables and random seating."""

    def __init__(self, tables: List[Table]) -> None:
        if not tables:
            raise ValueError("OpenSpace needs at least one table.")
        self.tables: List[Table] = tables

    def number_of_tables(self) -> int:
        """Return the number of tables."""
        return len(self.tables)

    def total_capacity(self) -> int:
        """Return total number of seats."""
        return sum(t.capacity for t in self.tables)

    def seats_left(self) -> int:
        """Return how many seats are still free."""
        return sum(t.left_capacity() for t in self.tables)

    def clear(self) -> None:
        """Remove everyone from all seats."""
        for table in self.tables:
            for seat in table.seats:
                seat.remove_occupant()

    def organize(self, names: Iterable[str], seed: int | None = None) -> Tuple[int, int]:
        """
        Randomly place people at tables, simple to follow:
        - clean names
        - shuffle
        - clear seats
        - assign name by name, table by table

        :param names: list/iterable of names (strings)
        :param seed: optional random seed for stable results
        :return: (placed_count, overflow_count)
        """
        clean: List[str] = [n.strip() for n in names if isinstance(n, str) and n.strip()]
        if not clean:
            return 0, 0

        rng = random.Random(seed)
        rng.shuffle(clean)

        self.clear()

        placed = 0
        cap = self.total_capacity()

        # Assign each name to the first table that has a free seat
        for name in clean:
            if placed >= cap:
                break
            assigned = False
            for table in self.tables:
                if table.assign_seat(name):
                    placed += 1
                    assigned = True
                    break
            if not assigned:
                break  # all tables full

        overflow = max(0, len(clean) - placed)
        return placed, overflow

    def display(self) -> None:
        """Print all tables and seats."""
        header = (
            f"Open Space — tables: {self.number_of_tables()}, "
            f"capacity: {self.total_capacity()}, seats left: {self.seats_left()}"
        )
        print(header)
        print("-" * len(header))
        for i, table in enumerate(self.tables, start=1):
            print(f"\nTable {i}:")
            table.show_table()

    def store(self, filename: str = "openspace.csv") -> Path:
        """Save the current seating to a CSV file."""
        path = Path(filename)
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Table", "Seat", "Name"])
            for ti, table in enumerate(self.tables, start=1):
                for si, seat in enumerate(table.seats, start=1):
                    name = seat.occupant if not seat.free else ""
                    writer.writerow([ti, si, name])
        print(f"Saved seating in: {filename}")
        return path
