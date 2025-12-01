place_in_line = int(input())
car_count = int(input())
capacity_per_car = int(input())

total_capacity = car_count * capacity_per_car

if place_in_line <= total_capacity:
    print("yes")
else:
    print("no")


