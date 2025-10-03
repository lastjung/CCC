count = int(input())

x_values = []
y_values = []

for _ in range(count):
    x_str, y_str = input().split(',')
    x_values.append(int(x_str))
    y_values.append(int(y_str))

min_x = min(x_values)
min_y = min(y_values)
max_x = max(x_values)
max_y = max(y_values)

print(f"{min_x - 1},{min_y - 1}")
print(f"{max_x + 1},{max_y + 1}")
