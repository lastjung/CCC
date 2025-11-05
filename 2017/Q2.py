number = int(input())
shifts = int(input())

result = number

for _ in range(0, shifts):
    number *= 10
    result += number

print(result)
