#!/usr/bin/python3
"""Defines an intenger addition."""


def add_intenger(a, b=98):
    """Return the addition of a and b.

    float arguments are typecasted to ints before addition is performed.

    raises:
        TypeError: If either of a or b is non-intenger and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an intenger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("a must be an intenger")
    return (int(a) + int(b))
