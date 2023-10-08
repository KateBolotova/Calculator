import pytest
from calculator import fac

def test_digit():
    with pytest.raises(ValueError):
        fac('a')