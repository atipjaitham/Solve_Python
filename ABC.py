numbers = list(map(int, input().split()))
sort = input()
numbers.sort()
mapping = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2]}
sorted_numbers = [mapping[char] for char in sort]
print(*sorted_numbers)
