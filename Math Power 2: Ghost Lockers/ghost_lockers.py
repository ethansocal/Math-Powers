from os import PathLike
from typing import Optional
from matplotlib import pyplot as plt
from tqdm import tqdm
import math


def main(
    csv_file: Optional[PathLike] = "raw_data.csv",
    plot: bool = True,
    locker_amount: int = 500,
) -> None:
    """Solve the math extra credit problem with brute forcing."""
    locker_amount += 1
    y = [500]
    lockers: dict[int, bool] = {}

    for locker in range(1, locker_amount):
        lockers[locker] = True

    for ghost in range(2, locker_amount):
        for locker in lockers:
            if (locker % ghost) == 0:
                lockers[locker] = not lockers[locker]

        count = 0

        for locker in lockers:
            if lockers[locker] is True:
                count += 1

        y.append(count)

    count = 0
    for locker in lockers:
        if lockers[locker] is True:
            count += 1

    if csv_file is not None:
        with open(csv_file, "w") as file:
            file.write("Ghost Number,Open Lockers\n")
            file.write(
                "\n".join([f"{index},{locker}" for index, locker in enumerate(y)])
            )

    if plot is True:
        plt.plot(list(range(1, locker_amount)), y)
        plt.title("Lockers over Ghost Iterations")
        plt.xlabel("Ghost")
        plt.ylabel("Open Lockers")
        plt.grid(True, "both", "both")
        plt.show()

    return count


def view_pattern(locker_limit: int = 500) -> None:
    results = []
    for i in tqdm(range(1, locker_limit + 1)):
        results.append(main(locker_amount=i, csv_file=None, plot=False))

    plt.plot(list(range(1, locker_limit + 1)), results)
    plt.title("Answer over locker amount")
    plt.xlabel("Locker Amount")
    plt.ylabel("Result")
    plt.grid(True, "both", "both")
    plt.show()


def confirm_pattern(locker_limit: int = 500) -> bool:
    for i in tqdm(range(1, locker_limit + 1)):
        if not main(locker_amount=i, csv_file=None, plot=False) == math.floor(
            math.sqrt(i)
        ):
            return False
    return True


if __name__ == "__main__":
    main()
