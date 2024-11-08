import pytest
import geo.arccos

def test_arccos():
    assert geo.arccos.arccos(0.1, 10) == pytest.approx(1.47063)
