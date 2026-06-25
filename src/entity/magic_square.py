def magic_constant(n: int) -> int:
    return n * (n * n + 1) // 2  # INV-1


def all_rows_sum_to(grid: list[list[int]], target: int) -> bool:
    return all(sum(row) == target for row in grid)  # INV-2


def all_cols_sum_to(grid: list[list[int]], target: int) -> bool:
    n = len(grid)
    return all(sum(grid[r][c] for r in range(n)) == target for c in range(n))  # INV-3


def diagonals_sum_to(grid: list[list[int]], target: int) -> bool:
    n = len(grid)
    main = sum(grid[i][i] for i in range(n))
    anti = sum(grid[i][n - 1 - i] for i in range(n))
    return main == target and anti == target  # INV-4


def values_valid(grid: list[list[int]]) -> bool:
    filled = [v for row in grid for v in row if v != 0]
    return all(1 <= v <= 16 for v in filled) and len(filled) == len(set(filled))  # INV-5


def has_single_zero_row_or_col(grid: list[list[int]]) -> bool:
    n = len(grid)
    row_counts = [sum(cell == 0 for cell in row) for row in grid]
    col_counts = [sum(grid[r][c] == 0 for r in range(n)) for c in range(n)]
    return any(c == 1 for c in row_counts) or any(c == 1 for c in col_counts)  # INV-7


def count_zeros(grid: list[list[int]]) -> int:
    return sum(cell == 0 for row in grid for cell in row)  # INV-6


def solve_blanks(grid: list[list[int]]) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    working = [row[:] for row in grid]
    magic = magic_constant(len(grid))
    while count_zeros(working) > 0:
        filled = False
        for r in range(len(working)):
            zeros = [c for c in range(len(working)) if working[r][c] == 0]
            if len(zeros) == 1:
                c = zeros[0]
                v = magic - sum(working[r][j] for j in range(len(working)) if j != c)
                working[r][c] = v
                result.append((r, c, v))
                filled = True  # AC-3
        if not filled:
            for c in range(len(working)):
                zeros = [r for r in range(len(working)) if working[r][c] == 0]
                if len(zeros) == 1:
                    r = zeros[0]
                    v = magic - sum(working[i][c] for i in range(len(working)) if i != r)
                    working[r][c] = v
                    result.append((r, c, v))
                    filled = True
        if not filled:
            break
    return result  # AC-1
