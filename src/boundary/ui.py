from src.entity.magic_square import validate_grid_shape


def parse_grid(raw) -> list[list[int]]:
    validate_grid_shape(raw)  # E-1
    return [row[:] for row in raw]
