def kg_to_pounds(kg):
    """Convert kilograms to pounds."""
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 2.20462


def pounds_to_kg(lb):
    """Convert pounds to kilograms."""
    if lb < 0:
        raise ValueError("Weight cannot be negative")
    return lb / 2.20462