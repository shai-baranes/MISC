def calculate_average(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    This function takes a list of numerical values and returns their average (arithmetic mean).
    If the input list is empty, a ValueError is raised.

    Parameters
    ----------
    numbers : list of float or int
        A list containing numeric values for which the average is to be calculated.

    Returns
    -------
    float
        The arithmetic mean of the input numbers.

    Raises
    ------
    ValueError
        If the input list is empty.

    Examples
    --------
    >>> calculate_average([1, 2, 3, 4])
    2.5

    >>> calculate_average([])
    Traceback (most recent call last):
        ...
    ValueError: The input list cannot be empty.
    """
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    return sum(numbers) / len(numbers)
