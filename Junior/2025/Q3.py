code_count = int(input())

for _ in range(code_count):
    original_code = input().strip()

    uppercase_part = []
    number_sum = 0
    current_number_str = ""

    for char in original_code:
        if char.isupper():
            uppercase_part.append(char)

        if char.isdigit():
            current_number_str += char
        else:
            if current_number_str:
                number_sum += int(current_number_str)
                current_number_str = ""

    if current_number_str:
        number_sum += int(current_number_str)

    updated_code = "".join(uppercase_part) + str(number_sum)
    print(updated_code)
