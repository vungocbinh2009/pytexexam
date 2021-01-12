import inspect


def ams_math_package() -> str:
    """
    Returns the command lines needed to type math formula in latex
    """
    return inspect.cleandoc(r"""
    \usepackage{amsmath}
    \usepackage{amsfonts}
    \usepackage{amssymb}
    """)
