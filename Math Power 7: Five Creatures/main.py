from itertools import permutations
from typing import Dict, Literal, Tuple

from rich import print
from rich.panel import Panel
from rich.table import Table

CREATURES = ["Goblin", "Witch", "Ghost", "Black Cat", "Bat"]
SOUNDS = ["Scream", "Hum", "Screech", "Whistle", "Giggle"]
PLACES = ["Attic", "Chimney", "First Floor", "Second Floor", "Basement"]

Creatures = Dict[
    Literal["Goblin", "Witch", "Ghost", "Black Cat", "Bat"],
    Tuple[
        Literal["Scream", "Hum", "Screech", "Whistle", "Giggle"],
        Literal["Attic", "Chimney", "First Floor", "Second Floor", "Basement"],
    ],
]


def rule_1(creatures: Creatures) -> bool:
    if creatures["Goblin"][1] != "Chimney" or creatures["Goblin"][0] in [
        "Giggle",
        "Whistle",
    ]:
        return False
    return True


def rule_2(creatures: Creatures) -> bool:
    if creatures["Ghost"][0] != "Scream":
        return False
    return True


def rule_3(creatures: Creatures) -> bool:
    if creatures["Black Cat"][1] != "Second Floor" or creatures["Bat"][1] != "First Floor":
        return False
    return True


def rule_4(creatures: Creatures) -> bool:
    for i in creatures.items():
        if i[1][1] == "Attic" and i[1][0] == "Hum":
            return True
    return False


def rule_5(creatures: Creatures) -> bool:
    for i in creatures.items():
        if i[1][1] == "First Floor" and i[1][0] != "Whistle":
            return True
    return False


RULES = [rule_1, rule_2, rule_3, rule_4, rule_5]


def display_result(creatures: Creatures):
    table = Table("Creature", "Sound", "Place", style="yellow")
    for i in creatures:
        table.add_row(i, creatures[i][0], creatures[i][1])

    return Panel(table, title="Solution", style="green")


def main():
    tries = 0
    successes = []
    for current_sounds in permutations(SOUNDS):
        for current_places in permutations(PLACES):
            creatures: Creatures = {}
            for index, i in enumerate(CREATURES):
                creatures[i] = (current_sounds[index], current_places[index])

            failed = []
            for rule in RULES:
                if rule(creatures) is False:
                    failed.append(rule.__name__)
            if len(failed) == 0:
                successes.append(display_result(creatures))
            else:
                exclude = ["rule_4"]
                if all([i not in failed for i in exclude]):
                    pass  # print(f"[red]Fail #{tries} {', '.join(failed)}[/]")
            tries += 1
    for i in successes:
        print(i)
    print(f"{len(successes)}/{tries} solutions found")

if __name__ == "__main__":
    main()
