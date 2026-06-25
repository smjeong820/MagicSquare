def magic_constant(n: int) -> int:
    return n * (n * n + 1) // 2  # INV-1


def all_rows_sum_to(grid: list[list[int]], target: int) -> bool:
    return all(sum(row) == target for row in grid)  # INV-2


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
                filled = True
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
