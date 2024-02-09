from pytexexam.jinja2env import jinja_env


def ams_math_package() -> str:
    """
    Returns the code needed to add in preamble to type math formula in latex
    """
    return jinja_env.get_template("latex_util/ams_math_package.tex").render()


def bold_title(text: str) -> str:
    """
    Create bold title in exam header

    :return: latex code
    """
    return jinja_env.get_template("latex_util/bold_title.tex").render(
        text=text
    )


def geometry_package(top: float, bottom: float, left: float, right: float) -> str:
    """
    Generate latex code to add geometry package

    :param top: top margin
    :param bottom: bottom margin
    :param left: left margin
    :param right: right margin
    """
    return jinja_env.get_template("latex_util/geometry_package.tex").render(
        top=top, bottom=bottom, left=left, right=right
    )


def add_multiple_package(package_list: list[str]) -> str:
    """
    Generate latex code to add multiple package to preamble

    :param package_list: List of package to add in preamble
    """
    return jinja_env.get_template("latex_util/add_multiple_package.tex").render(
        package_list=package_list
    )


def add_package_with_options(package: str, options: str) -> str:
    return jinja_env.get_template("latex_util/add_package_with_options.tex").render(
        options=options, package=package
    )
