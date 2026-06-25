import pytest

# SSOT: 4×4 완성 마방진 (모든 행·열·대각선 합 = 34)
COMPLETE_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# SSOT: 빈 칸(0) 정확히 2개 — 정답 (1,2)=11, (3,1)=15
PUZZLE_GRID = [
    [16, 3, 2, 13],
    [5, 10, 0, 8],
    [9, 6, 7, 12],
    [4, 0, 14, 1],
]


@pytest.fixture
def complete_grid():
    return [row[:] for row in COMPLETE_GRID]


@pytest.fixture
def puzzle_grid():
    return [row[:] for row in PUZZLE_GRID]
