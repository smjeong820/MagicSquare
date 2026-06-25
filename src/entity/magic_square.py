def magic_constant(n: int) -> int:
    return n * (n * n + 1) // 2  # INV-1


def count_zeros(grid: list[list[int]]) -> int:
    return sum(cell == 0 for row in grid for cell in row)  # INV-6
