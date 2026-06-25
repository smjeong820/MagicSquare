import pytest


@pytest.mark.boundary
def test_u_in_01_parse_grid_rejects_invalid_shape():
    # Given: None 또는 4×4가 아닌 격자
    # When: parse_grid 호출
    # Then: ValueError 거부 (E-1)
    pytest.fail("RED: U-IN-01 — 구현 없음, 의도적 실패")
