import string


def get_answer_key() -> list[str]:
    """
    get list of alphabet character. (to use it as answer key)
    :return: Alphabet character list.
    """
    return list(string.ascii_uppercase)


def get_alpha_numbering_key() -> list[str]:
    """
    get list of alphabet character for numbering
    :return: Alphabet character list.
    """
    return list(string.ascii_lowercase)
