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
