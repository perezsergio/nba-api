"""
Util functions used for filtering python matrices (lists of lists).

Functions:
    find_indices
    filter_matrix_by_column_indices
    filter_matrix_by_column_names

"""


def find_indices(a, b) -> list:
    """
    Find the indices of list a which return an element of list b.
    Usage example:
        a = [5, 6, 7]
        b = [5, 7]
        filter_indices(a,b) # [0,2]
    """
    return [i for i in range(len(a)) if a[i] in b]


def filter_matrix_by_column_indices(
    matrix: list[list], column_indices: list[int]
) -> list[list]:
    """
    Given a certain matrix, i.e. a list of lists, filter the columns with the specified indices.
    Usage example:
        m = [['year', 'price'], [2020, 20.50]]
        filter_matrix_by_column_indices(m, [0]) # [['year'], [2020]]
    """
    return [[el for i, el in enumerate(row) if i in column_indices] for row in matrix]


def filter_matrix_by_column_names(
    matrix: list[list], headers_of_interest: list
) -> list[list]:
    """
    Given a 2d matrix (list of lists) and a list of headers_of_interest,
    return the columns of the matrix corresponding to the headers of interest.
    Usage example:
        m = [['year', 'price'], [2020, 20.50]]
        filter_matrix_by_column_names(m, ['year']) # [['year'], [2020]]
    """

    # the headers are the first row of the matrix
    headers = matrix[0]

    # find the indices of the columns that we want to keep
    columns_of_interest = find_indices(headers, headers_of_interest)

    # only keep the columns with the right indices
    filtered_matrix = filter_matrix_by_column_indices(
        matrix, column_indices=columns_of_interest
    )

    return filtered_matrix
