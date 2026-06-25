import pytest

from src.entity.magic_square import (
    all_cols_sum_to,
    all_rows_sum_to,
    count_zeros,
    diagonals_sum_to,
    magic_constant,
    solve_blanks,
)
from tests._approval import assert_matches_golden


@pytest.mark.entity
def test_d_msq_01_magic_constant_is_34():
    # Given: 4×4 마방진 (n = 4)
    # When:  magic_constant(4) 호출
    # Then:  반환값 == 34 (golden master)
    result = magic_constant(4)
    assert result == 34
    assert_matches_golden(str(result), "d_msq_01_magic_constant_n4.approved.txt")


@pytest.mark.entity
def test_d_msq_02_all_rows_sum_to_complete_grid(complete_grid):
    # Given: 완성 4×4 마방진 격자, target=34
    # When:  all_rows_sum_to(complete_grid, 34) 호출
    # Then:  모든 행 합 == 34
    assert all_rows_sum_to(complete_grid, 34)


@pytest.mark.entity
def test_d_msq_03_all_cols_sum_to_complete_grid(complete_grid):
    # Given: 완성 4×4 마방진 격자, target=34
    # When:  all_cols_sum_to(complete_grid, 34) 호출
    # Then:  모든 열 합 == 34
    assert all_cols_sum_to(complete_grid, 34)


@pytest.mark.entity
def test_d_msq_04_diagonals_sum_to_complete_grid(complete_grid):
    # Given: 완성 4×4 마방진 격자, target=34
    # When:  diagonals_sum_to(complete_grid, 34) 호출
    # Then:  주·부대각선 합 == 34
    assert diagonals_sum_to(complete_grid, 34)


@pytest.mark.entity
def test_d_msq_05_values_valid_complete_grid(complete_grid):
    # Given: 완성 4×4 마방진 격자
    # When:  values_valid(complete_grid) 호출
    # Then:  1~16 중복 없음
    pytest.fail("RED: D-MSQ-05 — 구현 없음, 의도적 실패")


@pytest.mark.entity
def test_d_msq_06_count_zeros_is_2(puzzle_grid):
    # Given: 빈 칸 2개인 4×4 퍼즐 격자
    # When:  count_zeros(puzzle_grid) 호출
    # Then:  반환값 == 2
    assert count_zeros(puzzle_grid) == 2


@pytest.mark.entity
def test_d_msq_08_solve_blanks_returns_two_pairs(puzzle_grid):
    # Given: 빈 칸 2개인 4×4 퍼즐 격자 (SSOT)
    # When:  solve_blanks(puzzle_grid) 호출
    # Then:  (행, 열, 값) 2쌍 — (1,2,11), (3,1,15)
    assert solve_blanks(puzzle_grid) == [(1, 2, 11), (3, 1, 15)]
