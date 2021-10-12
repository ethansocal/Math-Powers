from rich.console import Console
from rich.table import Table

"""Solve the math extra credit problem with brute forcing."""
LOCKER_AMOUNT = 50  # Number of lockers
# Create a table of lockers and whether they are open or not
lockers: dict[int, bool] = {}

for locker in range(1, LOCKER_AMOUNT + 1):
    lockers[locker] = True  # Start every locker as open, or True

for ghost in range(2, LOCKER_AMOUNT + 1):
    # Loop through every ghost between 2 and the amount of lockers
    for locker in lockers:
        if (locker % ghost) == 0:
            # If the modulus of the locker number by the ghost number is 0,
            # reverse the status of the locker
            lockers[locker] = not lockers[locker]

table = Table(title="Lockers")

table.add_column("Locker Number", justify="right", style="blue")
table.add_column("Status", justify="left")

for locker in lockers:
    table.add_row(f"#{locker}", "x" if lockers[locker] is True else " ")

console = Console()
console.print(table)
