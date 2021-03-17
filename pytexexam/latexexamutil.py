import inspect


def ams_math_package() -> str:
    """
    Returns the code needed to add in preamble to type math formula in latex
    """
    return inspect.cleandoc(r"""
    \usepackage{amsmath}
    \usepackage{amsfonts}
    \usepackage{amssymb}
    """)
