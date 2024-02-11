from pytexexam.jinja2env import jinja_env


def two_column_header(left: str, right: str, col_alignment=r"\centering") -> str:
    """
    Create exam header with two column

    :param left: left text
    :param right: right text
    :param col_alignment: Column alignment: Options: \raggedleft, \centering, \raggedright,
    :return: Latex code
    """
    return jinja_env.get_template("latex_util/two_column_header.tex").render(
        col_alignment=col_alignment,
        left=left,
        right=right
    )
