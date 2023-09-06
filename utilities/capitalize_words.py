def capitalize_words_and_remove_und_scr(input_word: str) -> str:
    """
    Capitalizes words and inserts space instead of an underscore
    """
    words = input_word.split("_")
    capitalized_words = [word.capitalize() for word in words]

    if len(input_word) <= 4 and input_word != 'date':
        capitalized_words = [word.upper() for word in words]
    else:
        capitalized_words = [word.capitalize() for word in words]

    output_str = " ".join(capitalized_words)
    return output_str
