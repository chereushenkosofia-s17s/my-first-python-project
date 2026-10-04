n = int(input())

binary = format(n, "08b")

if binary == binary[::-1]:
    print("True")
else:
    print("False")