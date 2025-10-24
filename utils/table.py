from typing import List


class Seat:
    """Class that represents one seat."""

    def __init__(self) -> None:
        # Seat starts empty
        self.free: bool = True
        self.occupant: str = ""

    def set_occupant(self, name: str) -> bool:
        """
        Give this seat to a person if the seat is free.
        Returns True if it worked, False otherwise.
        """
        if self.free and isinstance(name, str) and name.strip():
            self.occupant = name.strip()
            self.free = False
            return True
        return False

    def remove_occupant(self) -> str:
        """
        Remove the current person from the seat.
        Returns the name that was removed (or empty string).
        """
        previous: str = self.occupant
        self.occupant = ""
        self.free = True
        return previous

    def __str__(self) -> str:
        """Show the name if occupied, otherwise 'empty'."""
        return self.occupant if not self.free else "empty"


class Table:
    """Class that defines a table with a few seats."""

    def __init__(self, capacity: int = 4, name: str = "Table") -> None:
        # Make sure capacity makes sense
        if capacity <= 0:
            raise ValueError("Capacity must be > 0.")

        self.capacity: int = capacity
        self.name: str = name
        # Create the seats for this table
        self.seats: List[Seat] = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:
        """Check if this table still has a free seat."""
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        """
        Try to give a seat to this person at this table.
        Returns True if it worked, False if the table is full.
        """
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        return False

    def left_capacity(self) -> int:
        """Count how many free seats are left."""
        return sum(1 for seat in self.seats if seat.free)

    def show_table(self) -> None:
        """Print the table and who sits where."""
        print(f"{self.name} — free seats: {self.left_capacity()}/{self.capacity}")
        for i, seat in enumerate(self.seats, start=1):
            person = seat.occupant if not seat.free else "empty"
            print(f"  Seat {i}: {person}")

    def __str__(self) -> str:
        """Return a single line with all seats."""
        people = ", ".join(str(seat) for seat in self.seats)
        return f"{self.name} [{people}]"
