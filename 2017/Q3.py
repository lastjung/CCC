
start_point = [int(value) for value in input().split()]
end_point = [int(value) for value in input().split()]

steps = int(input())

distance = abs(start_point[0] - end_point[0]) 
distance += abs(start_point[1] - end_point[1])

if steps >= distance and (steps - distance) % 2 == 0:
    print("Y")
else:
    print("N")
