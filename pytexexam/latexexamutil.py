import inspect
from typing import List


def ams_math_package() -> str:
    """
    Returns the code needed to add in preamble to type math formula in latex
    """
    return inspect.cleandoc(r"""
    \usepackage{amsmath}
    \usepackage{amsfonts}
    \usepackage{amssymb}
    
    """)


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


def bold_title(text: str) -> str:
    """
    Create bold title in exam header

    :return: latex code
    """
    return inspect.cleandoc(rf"""
    \begin{{center}}
    \textbf {{ {{\Large {text} }} }}
    \end{{center}}
    
    """)


def geometry_package(top: float, bottom: float, left: float, right: float) -> str:
    """
    Generate latex code to add geometry package

    :param top: top margin
    :param bottom: bottom margin
    :param left: left margin
    :param right: right margin
    """
    return rf"""
        \usepackage[left = {left}cm, right = {right}cm, top = {top}cm, bottom = {bottom}cm]{{geometry}}
        
    """


def add_multiple_package(package_list: List[str]) -> str:
    """
    Generate latex code to add multiple package to preamble

    :param package_list: List of package to add in preamble
    """
    usepackage_command_list = []
    for package in package_list:
        usepackage_command_list.append(rf"""\usepackage{{{package}}}""")

    return "\n".join(usepackage_command_list) + "\n"
