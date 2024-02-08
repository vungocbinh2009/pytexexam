import inspect


def two_column_header(left: str, right: str) -> str:
    """
    Create exam header with two column

    :param left: left text
    :param right: right text
    :return: Latex code
    """
    return inspect.cleandoc(rf"""
    \begin{{tabular}}{{ *{{2}}{{ p{{ \dimexpr0.5\linewidth-2\tabcolsep\relax }} }} }}
    {left} & {right}
    \end{{tabular}}
    """)