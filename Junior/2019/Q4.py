import sys


def horizontal_flip(grid):
    # Swap top and bottom rows.
    return [grid[1], grid[0]]


def vertical_flip(grid):
    # Swap left and right columns.
    return [[grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]]


def main() -> None:
    flips = sys.stdin.readline().strip()

    grid = [[1, 2], [3, 4]]

    for flip in flips:
        if flip == "H":
            grid = horizontal_flip(grid)
        else:
            grid = vertical_flip(grid)

    print(f"{grid[0][0]} {grid[0][1]}")
    print(f"{grid[1][0]} {grid[1][1]}")


if __name__ == "__main__":
    main()

# bash -lc 'cd /Users/eric/PG/CCC && for infile in Junior/2019/j4/*.in; do base=${infile%.in}; outfile="$base.out"; echo "Testing ${infile}"; diff -u "$outfile" <(python3 Junior/2019/Q4.py < "$infile") || exit 1; done'
