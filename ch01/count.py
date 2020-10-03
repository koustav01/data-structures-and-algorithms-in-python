def count(data, target):
    n = 0
    for item in data:
        if item == target:  # found a match
            n += 1
    return n

data=[int(x) for x in input().split()]
target=int(input())
ans=count(data , target)
print(ans)
