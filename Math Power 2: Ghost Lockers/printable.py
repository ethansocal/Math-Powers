"""Solve the math extra credit problem with brute forcing."""
LOCKER_AMOUNT = 500  # Number of lockers
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

count = 0
for locker in lockers:
    # For every locker, if it is open, add 1 to a count
    if lockers[locker] is True:
        count += 1

print(count)  # Display the count
