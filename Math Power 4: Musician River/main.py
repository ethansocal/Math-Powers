from rich import print
from rich.traceback import install
from rich.table import Table
from rich.console import Console

install()
console = Console()

PEOPLE = ["john", "paul", "george", "ringo"]
PEOPLE_TIMES = {"john": 1, "paul": 2, "george": 5, "ringo": 10, None: -1}
MAX_TIME = 17


def slowest_time(person1: str, person2: str = None) -> int:
    return max(PEOPLE_TIMES[person1], PEOPLE_TIMES[person2])


def display_result(result: tuple[list[str], int]):
    left = ["J", "P", "G", "R"]
    right = []
    table = Table(show_footer=True)
    table.add_column("Start", style="red")
    table.add_column("River", style="bright_blue")
    table.add_column("End", style="green", footer="[green]" + (" ".join(left.copy())))
    table.add_column(
        "Minutes", style="bright_yellow", footer="[bright_yellow]" + str(result[1])
    )
    for index, i in enumerate(result[0]):
        table.add_row(
            " ".join(left),
            ("<-- " if index % 2 == 1 else "")
            + (
                " ".join([ii[0].upper() for ii in i[4:].split(" + ")])
                if index % 2 == 0
                else i[4].upper()
            )
            + (" -->" if index % 2 == 0 else ""),
            " ".join(right),
            str(
                slowest_time(i[4:])
                if index % 2 == 1
                else slowest_time(*(i[4:].split(" + ")))
            ),
        )
        if index % 2 == 0:
            left.remove([ii[0] for ii in i[4:].split(" + ")][0].upper())
            left.remove([ii[0] for ii in i[4:].split(" + ")][1].upper())
            right.append([ii[0] for ii in i[4:].split(" + ")][0].upper())
            right.append([ii[0] for ii in i[4:].split(" + ")][1].upper())
        else:
            right.remove(i[4].upper())
            left.append(i[4].upper())
    return table


def see_rich_results(results: list[tuple[list[str], int]]) -> Table:
    max_length = max([len(i[0]) for i in results])
    table = Table()
    table.add_column("Time", style="bright_yellow")
    for i in range(max_length):
        if i % 2 == 0:
            table.add_column("-->", style="green")
        else:
            table.add_column("<--", style="red")

    for i in results:
        table.add_row(str(i[1]), *[ii[4:].title() for ii in i[0]])
    return table


def recursive():
    successes = []
    fails = []

    def func(
        time: int, at_dock: bool, right: list[str], left: list[str], chain: list
    ) -> bool:
        if time > MAX_TIME:
            fails.append(
                (
                    chain,
                    sum(
                        [
                            (
                                slowest_time(i[4:])
                                if index % 2 == 1
                                else slowest_time(*(i[4:].split(" + ")))
                            )
                            for index, i in enumerate(chain)
                        ]
                    ),
                )
            )
            return
        if len(left) == 4:
            successes.append(
                (
                    chain,
                    sum(
                        [
                            (
                                slowest_time(i[4:])
                                if index % 2 == 1
                                else slowest_time(*(i[4:].split(" + ")))
                            )
                            for index, i in enumerate(chain)
                        ]
                    ),
                )
            )
            return
        if at_dock:
            for person1 in right:
                for person2 in right:
                    if person1 != person2:
                        tempright = right.copy()
                        tempright.remove(person1)
                        tempright.remove(person2)
                        templeft = left.copy()
                        templeft.append(person1)
                        templeft.append(person2)
                        tempchain = chain.copy()
                        tempchain.append(f"--> {person1} + {person2}")
                        func(
                            time + slowest_time(person1, person2),
                            False,
                            tempright,
                            templeft,
                            tempchain,
                        )

        else:
            for person in left:
                templeft = left.copy()
                templeft.remove(person)
                tempright = right.copy()
                tempright.append(person)
                tempchain = chain.copy()
                tempchain.append(f"<-- {person}")
                func(time + slowest_time(person), True, tempright, templeft, tempchain)

    func(0, True, PEOPLE, [], [])
    console.clear()
    console.rule("[underline green]Solutions")
    print(see_rich_results(successes))
    console.rule("[underline bright_blue]Example Solution[/]")
    print(
        display_result(successes[__import__("random").randint(0, len(successes) - 1)])
    )
    print(
        f"{len(successes)}/{len(successes) + len(fails)} combinations were successful."
    )


if __name__ == "__main__":
    recursive()
