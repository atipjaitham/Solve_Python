scores = 0
for score in range(3):
    score = int(input())
    scores += score

if scores >= 80:
    print("A")
elif scores >= 75:
    print("B+")
elif scores >= 70:
    print("B")
elif scores >= 65:
    print("C+")
elif scores >= 60:
    print("C")
elif scores >= 55:
    print("D+")
elif scores >= 50:
    print("D")
else:
    print("F")
