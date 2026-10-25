def km_to_miles(km):
    """Convert kilometers to miles."""
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return km * 0.621371


def meters_to_feet(m):
    """Convert meters to feet."""
    if m < 0:
        raise ValueError("Distance cannot be negative")
    return m * 3.28084