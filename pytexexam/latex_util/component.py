from pytexexam.jinja2env import jinja_env


def two_column_header(left: str, right: str) -> str:
    """
    Create exam header with two column

    :param left: left text
    :param right: right text
    :return: Latex code
    """
    return jinja_env.get_template("latex_util/two_column_header.tex").render(
        left=left,
        right=right
    )
