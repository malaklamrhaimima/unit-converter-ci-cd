import pytest
from converter.weight import kg_to_pounds, pounds_to_kg


def test_kg_to_pounds_normal():
    assert kg_to_pounds(10) == pytest.approx(22.0462)


def test_pounds_to_kg_zero():
    assert pounds_to_kg(0) == 0


def test_negative_weight_raises():
    with pytest.raises(ValueError):
        kg_to_pounds(-1)