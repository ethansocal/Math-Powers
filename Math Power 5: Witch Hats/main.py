from itertools import permutations
from rich import print

for i in permutations(["white", "white", "black", "black", "black"], 3):
    drew = i[0]
    emily = i[1]
    gabe = i[2]

    if gabe == "white" and drew == "white":
        print("fail")
        continue
    if emily == "white" and gabe == "white":
        print("fail")
        continue
    print(drew, emily, gabe)