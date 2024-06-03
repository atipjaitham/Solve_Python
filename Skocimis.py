kangaroo = list(map(int, input().split()))
print(max((kangaroo[1]-kangaroo[0]-1), (kangaroo[2]-kangaroo[1]-1)))
