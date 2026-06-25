from src.entity.magic_square import validate_cell_values, validate_grid_shape, validate_zero_count


def parse_grid(raw) -> list[list[int]]:
    validate_grid_shape(raw)  # E-1
    grid = [row[:] for row in raw]
    validate_zero_count(grid)  # E-2
    validate_cell_values(grid)  # E-3
    return grid
