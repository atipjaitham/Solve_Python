import math
# c**2 = a**2 + b**2
a, b = list(map(float, input().split()))
c = math.sqrt(a**2+b**2)
print(f"{c:.6f}")
