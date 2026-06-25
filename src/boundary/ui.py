from src.entity.magic_square import (
    all_cols_sum_to,
    all_rows_sum_to,
    diagonals_sum_to,
    is_valid_candidate,
    magic_constant,
    solve_blanks,
    validate_cell_values,
    validate_grid_shape,
    validate_no_duplicate_nonzero,
    validate_zero_count,
    values_valid,
)


def blank_positions(grid: list[list[int]]) -> frozenset[tuple[int, int]]:
    return frozenset((r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 0)


def parse_grid(raw) -> list[list[int]]:
    validate_grid_shape(raw)  # E-1
    grid = [row[:] for row in raw]
    validate_zero_count(grid)  # E-2
    validate_cell_values(grid)  # E-3
    validate_no_duplicate_nonzero(grid)  # E-4
    return grid


def format_blanks(pairs: list[tuple[int, int, int]]) -> str:
    return ", ".join(str(v) for _, _, v in pairs)  # AC-5


def solve_puzzle_output(raw) -> str:
    grid = parse_grid(raw)
    pairs = solve_blanks(grid)  # AC-1
    return format_blanks(pairs)  # AC-5


def submit_puzzle(puzzle_template: list[list[int]], user_grid: list[list[int]]) -> str:
    """빈 칸만 채운 제출을 검증하거나, 빈 칸이 비어 있으면 정답을 반환한다."""
    validate_grid_shape(user_grid)  # E-1
    validate_cell_values(user_grid)  # E-3
    blanks = blank_positions(puzzle_template)
    for r in range(4):
        for c in range(4):
            if (r, c) not in blanks and user_grid[r][c] != puzzle_template[r][c]:
                raise ValueError("fixed cell modified")  # E-1
    expected_pairs = solve_blanks(puzzle_template)  # AC-1
    expected = {(r, c): v for r, c, v in expected_pairs}
    if all(user_grid[r][c] == 0 for r, c in blanks):
        return format_blanks(expected_pairs)  # AC-5
    for r, c in blanks:
        if user_grid[r][c] == 0:
            raise ValueError("incomplete blanks")  # E-2
        if user_grid[r][c] != expected[r, c]:
            raise ValueError("wrong answer")  # E-5
    target = magic_constant(4)
    if not all_rows_sum_to(user_grid, target):
        raise ValueError("row sum violation")
    if not all_cols_sum_to(user_grid, target):
        raise ValueError("col sum violation")
    if not diagonals_sum_to(user_grid, target):
        raise ValueError("diagonal sum violation")
    if not values_valid(user_grid):
        raise ValueError("values invalid")
    return format_blanks([(r, c, user_grid[r][c]) for r, c, _ in expected_pairs])  # AC-5


def evaluate_submission(puzzle_template: list[list[int]], user_grid: list[list[int]]) -> str:
    """제출 결과: 'correct', 'wrong', 'incomplete'."""
    validate_grid_shape(user_grid)  # E-1
    validate_cell_values(user_grid)  # E-3
    blanks = blank_positions(puzzle_template)
    for r in range(4):
        for c in range(4):
            if (r, c) not in blanks and user_grid[r][c] != puzzle_template[r][c]:
                return "wrong"
    expected_pairs = solve_blanks(puzzle_template)
    expected = {(r, c): v for r, c, v in expected_pairs}
    if any(user_grid[r][c] == 0 for r, c in blanks):
        return "incomplete"
    for r, c in blanks:
        if user_grid[r][c] != expected[r, c]:
            return "wrong"
    target = magic_constant(4)
    if not all_rows_sum_to(user_grid, target):
        return "wrong"
    if not all_cols_sum_to(user_grid, target):
        return "wrong"
    if not diagonals_sum_to(user_grid, target):
        return "wrong"
    if not values_valid(user_grid):
        return "wrong"
    return "correct"
