

def is_magic_square(square):
    """Return True if all row and column sums match."""
    target = sum(square[0])
    if any(sum(row) != target for row in square):
        return False
    for column in range(4):
        if sum(square[row][column] for row in range(4)) != target:
            return False
    return True


# grid = [[int(value) for value in input().split()] for _ in range(4)]
grid = []

for _ in range(4):
   one_line = [int(value) for value in input().split()]
   grid.append(one_line) 

print("magic" if is_magic_square(grid) else "not magic")
