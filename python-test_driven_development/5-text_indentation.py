#!/usr/bin/python3

"""Module for 5-text_indentation method"""


def text_indentation(text):
    """Method text_indentation prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: the text to print with 2 new lines

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(result, end="")


if __name__ == "__main__":
    import doctext
    doctext.textfile("tests/5-text_indentation.txt")
        