prev_direction = None
results = []

digit_str = input()

while digit_str != '99999':
    first_two = digit_str[:2]
    last_three = digit_str[2:]

    digit_sum = int(first_two[0]) + int(first_two[1])

    if digit_sum == 0 and prev_direction is not None:
        direction = prev_direction
    elif digit_sum % 2 == 0:
        direction = 'right'
    else:
        direction = 'left'

    steps = int(last_three)

    results.append(f"{direction} {steps}")

    prev_direction = direction
    digit_str = input()

for result in results:
    print(result)
