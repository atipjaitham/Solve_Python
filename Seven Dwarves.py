import pydash
dwarves = [int(input()) for _ in range(9)]
total = pydash.sum_(dwarves)
for i in dwarves:
    for j in dwarves:
        if ((total - (i + j)) == 100):
            if len(dwarves) == 9:
                pydash.pull(dwarves, i, j)
for i in (dwarves):
    print(*[i])
