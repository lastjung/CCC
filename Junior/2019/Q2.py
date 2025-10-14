line_count = int(input())

instructions = []

for _ in range(line_count):
    repeat, character = input().split()
    instructions.append(character * int(repeat))

for i in instructions:
    print(i)
