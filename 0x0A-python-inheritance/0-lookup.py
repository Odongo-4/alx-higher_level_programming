#!/usr/bin/python3
"""Defines an object variable using lookup method."""


def lookup(obj):
    """Returns a list of an object's available variables."""
    return (dir(obj))
