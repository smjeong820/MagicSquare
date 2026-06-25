import pytest

from src.boundary.ui import parse_grid


@pytest.mark.boundary
def test_u_in_01_parse_grid_rejects_invalid_shape():
    # Given: None 또는 4×4가 아닌 격자
    invalid_inputs = [
        None,
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]
    # When / Then: parse_grid → ValueError (E-1)
    for raw in invalid_inputs:
        with pytest.raises(ValueError):
            parse_grid(raw)


@pytest.mark.boundary
def test_u_in_02_parse_grid_rejects_wrong_zero_count():
    # Given: 0 개수가 2가 아닌 4×4 격자
    no_zeros = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    one_zero = [[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    three_zeros = [[0, 0, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # When / Then: parse_grid → ValueError (E-2)
    for raw in (no_zeros, one_zero, three_zeros):
        with pytest.raises(ValueError):
            parse_grid(raw)


@pytest.mark.boundary
def test_u_in_03_parse_grid_rejects_out_of_range_values():
    # Given: -1 또는 17이 포함된 4×4 격자 (0 두 개)
    # When: parse_grid 호출
    # Then: ValueError 거부 (E-3)
    pytest.fail("RED: U-IN-03 — 구현 없음, 의도적 실패")
