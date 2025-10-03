limit = int(input())
initial_infected = int(input())
spread_factor = int(input())

total_infected = initial_infected
current_day_infections = initial_infected
day = 0

while total_infected <= limit:
    day += 1
    current_day_infections *= spread_factor
    total_infected += current_day_infections

print(day)
