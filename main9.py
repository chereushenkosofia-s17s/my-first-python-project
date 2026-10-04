n = input()

result = ""

for digit in n:
    if int(digit) % 2 == 0:
        result += "*"
    else:
        result += digit

print(result)