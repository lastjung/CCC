line_count = int(input())


for _ in range(line_count):
    line = input().rstrip("\n")
    encoded_parts = []
    run_char = line[0]
    run_length = 1

    for char in line[1:]:
        if char == run_char:
            run_length += 1
        else:
            encoded_parts.append(f"{run_length} {run_char}")
            run_char = char
            run_length = 1

    encoded_parts.append(f"{run_length} {run_char}")
    print(" ".join(encoded_parts))
