problems = int(input())
answers = list(input())
scores = {"Adrian": 0, "Bruno": 0, "Goran": 0}

adrian_asw = "ABC" * problems
bruno_asw = "BABC" * problems
goran_asw = "CCAABB" * problems

for i in range(problems):
    if answers[i] == adrian_asw[i]:
        scores["Adrian"] += 1
    if answers[i] == bruno_asw[i]:
        scores["Bruno"] += 1
    if answers[i] == goran_asw[i]:
        scores["Goran"] += 1
max_scores = max(scores.values())
max_names = [name for name, scores in scores.items() if scores == max_scores]
max_names.sort()
print(max_scores)
for name in max_names:
    print(name)
