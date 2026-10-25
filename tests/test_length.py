import pytest
from converter.length import km_to_miles, meters_to_feet


def test_km_to_miles_normal():
    assert km_to_miles(10) == pytest.approx(6.21371)


def test_meters_to_feet_zero():
    assert meters_to_feet(0) == 0


def test_km_to_miles_negative_raises():
    with pytest.raises(ValueError):
        km_to_miles(-5)