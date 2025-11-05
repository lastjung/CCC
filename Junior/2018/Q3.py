def distance_table(segment_lengths):
    """Return the pairwise distances between consecutive cities."""
    totals = [0]
    for segment in segment_lengths:
        totals.append(totals[-1] + segment)

    size = len(totals)
    table = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(abs(totals[j] - totals[i]))
        table.append(row)
    return table


distances = [int(value) for value in input().split()]

for row in distance_table(distances):
    print(" ".join(str(value) for value in row))
