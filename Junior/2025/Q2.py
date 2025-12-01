donuts_available = int(input())
event_count = int(input())

for _ in range(event_count):
    operation = input().strip()
    quantity = int(input())

    if operation == "+":
        donuts_available += quantity
    else:
        donuts_available -= quantity

print(donuts_available)
