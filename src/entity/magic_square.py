def validate_zero_count(grid: list[list[int]]) -> None:
    if count_zeros(grid) != 2:
        raise ValueError("grid must have exactly 2 zeros")  # E-2


def validate_cell_values(grid: list[list[int]]) -> None:
    for row in grid:
        for v in row:
            if not isinstance(v, int) or v < 0 or v > 16:
                raise ValueError("cell values must be 0 or 1-16")  # E-3


def validate_no_duplicate_nonzero(grid: list[list[int]]) -> None:
    filled = [v for row in grid for v in row if v != 0]
    if len(filled) != len(set(filled)):
        raise ValueError("duplicate non-zero values")  # E-4


def is_valid_candidate(grid: list[list[int]], row: int, col: int, value: int) -> bool:
    target = magic_constant(len(grid))
    row_sum = sum(value if c == col else grid[row][c] for c in range(len(grid)))
    return row_sum == target  # E-5


def validate_grid_shape(grid) -> None:
    if grid is None:
        raise ValueError("grid must be 4x4")  # E-1
    if not isinstance(grid, list) or len(grid) != 4:
        raise ValueError("grid must be 4x4")  # E-1
    for row in grid:
        if not isinstance(row, list) or len(row) != 4:
            raise ValueError("grid must be 4x4")  # E-1


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


def filled_grid(grid: list[list[int]], pairs: list[tuple[int, int, int]]) -> list[list[int]]:
    result = [row[:] for row in grid]
    for r, c, v in pairs:
        result[r][c] = v
    return result  # AC-2


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


# SSOT: tests/conftest.py COMPLETE_GRID
_COMPLETE_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# SSOT: tests/conftest.py PUZZLE_GRID — generate 실패 시 폴백
_PUZZLE_FALLBACK = [
    [16, 3, 2, 13],
    [5, 10, 0, 8],
    [9, 6, 7, 12],
    [4, 0, 14, 1],
]


def _permute_rows_cols(grid: list[list[int]], rng) -> list[list[int]]:
    rows = list(range(4))
    cols = list(range(4))
    rng.shuffle(rows)
    rng.shuffle(cols)
    return [[grid[r][c] for c in cols] for r in rows]


def _mask_cells(complete: list[list[int]], cells: list[tuple[int, int]]) -> list[list[int]]:
    puzzle = [row[:] for row in complete]
    for r, c in cells:
        puzzle[r][c] = 0
    return puzzle


def is_valid_puzzle(puzzle: list[list[int]]) -> bool:
    if count_zeros(puzzle) != 2:
        return False
    if not has_single_zero_row_or_col(puzzle):
        return False
    pairs = solve_blanks(puzzle)
    if len(pairs) != 2:
        return False
    completed = filled_grid(puzzle, pairs)
    target = magic_constant(4)
    return (
        all_rows_sum_to(completed, target)
        and all_cols_sum_to(completed, target)
        and diagonals_sum_to(completed, target)
        and values_valid(completed)
    )


def generate_puzzle(rng=None) -> list[list[int]]:
    import random

    rng = rng or random.Random()
    complete = _permute_rows_cols(_COMPLETE_GRID, rng)
    positions = [(r, c) for r in range(4) for c in range(4)]
    rng.shuffle(positions)
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            candidate = _mask_cells(complete, [positions[i], positions[j]])
            if is_valid_puzzle(candidate):
                return candidate
    return [row[:] for row in _PUZZLE_FALLBACK]
