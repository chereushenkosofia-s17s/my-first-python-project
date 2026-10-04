k = int(input())

day = (k - 1) % 7

if day == 5 or day == 6:
    print("day off")
else:
    print("working day")