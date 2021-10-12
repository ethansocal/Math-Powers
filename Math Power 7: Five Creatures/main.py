from itertools import permutations
from typing import Dict, Literal, Tuple

from rich import print
from rich.panel import Panel
from rich.table import Table

CREATURES = ["goblin", "witch", "ghost", "blackcat", "bat"]
SOUNDS = ["scream", "hum", "screech", "whistle", "giggle"]
PLACES = ["attic", "chimney", "firstfloor", "secondfloor", "basement"]

Creatures = Dict[
    Literal["goblin", "witch", "ghost", "blackcat", "bat"],
    Tuple[
        Literal["scream", "hum", "screech", "whistle", "giggle"],
        Literal["attic", "chimney", "firstfloor", "secondfloor", "basement"],
    ],
]


def rule_1(creatures: Creatures) -> bool:
    if creatures["goblin"][1] != "chimney" or creatures["goblin"][0] in [
        "giggle",
        "whistle",
    ]:
        return False
    return True


def rule_2(creatures: Creatures) -> bool:
    if creatures["ghost"][0] != "scream":
        return False
    return True


def rule_3(creatures: Creatures) -> bool:
    if creatures["blackcat"][1] != "secondfloor" or creatures["bat"][1] != "firstfloor":
        return False
    return True


def rule_4(creatures: Creatures) -> bool:
    for i in creatures.items():
        if i[1][1] == "attic" and i[1][0] == "hum":
            return True
    return False


def rule_5(creatures: Creatures) -> bool:
    for i in creatures.items():
        if i[1][1] == "firstfloor" and i[1][0] != "whistle":
            return True
    return False


RULES = [rule_1, rule_2, rule_3, rule_4, rule_5]


def display_result(creatures: Creatures):
    table = Table("Creature", "Sound", "Place")
    for i in creatures:
        table.add_row(i, creatures[i][0], creatures[i][1])

    return Panel(table)


def main():
    tries = 0
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
                print(display_result(creatures))
            else:
                tries += 1
                exclude = ["rule_4"]
                if all([i not in failed for i in exclude]):
                    pass  # print(f"[red]Fail #{tries} {', '.join(failed)}[/]")


if __name__ == "__main__":
    main()
