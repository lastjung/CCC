def count_occupied_both(day_one, day_two):
    """Return how many spots stayed occupied on both days."""
    
    return sum(1 for first, second in zip(day_one, day_two) if first == second == "C")


_ = int(input())
day_one = input().strip()
day_two = input().strip()

print(count_occupied_both(day_one, day_two))
