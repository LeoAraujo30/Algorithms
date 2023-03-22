def validate_word(string):
    if string:
        return True
    else:
        return False


def is_palindrome_recursive(word, low_index, high_index):
    if not validate_word(word):
        return False

    if 0 <= low_index <= len(word) - 1 and 0 <= high_index <= len(word) - 1:
        if word[low_index] == word[high_index]:
            bool = is_palindrome_recursive(word, low_index + 1, high_index - 1)
            return bool

        else:
            return False

    return True
