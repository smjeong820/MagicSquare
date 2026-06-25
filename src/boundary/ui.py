from src.entity.magic_square import (
    is_valid_candidate,
    solve_blanks,
    validate_cell_values,
    validate_grid_shape,
    validate_no_duplicate_nonzero,
    validate_zero_count,
)


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
