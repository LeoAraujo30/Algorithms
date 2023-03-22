# Funções merge e merge_sort foram tiradas do course da Trybe
# Dia 3 da seção 4 no modulo de Ciência da Computação

def merge(letters, start, mid, end):
    left = letters[start:mid]
    right = letters[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            letters[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            letters[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            letters[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            letters[general_index] = right[right_index]
            right_index = right_index + 1


def merge_sort(letters, start=0, end=None):
    if end is None:
        end = len(letters)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(letters, start, mid)
        merge_sort(letters, mid, end)
        merge(letters, start, mid, end)


def get_word(word):
    string = ""
    for letter in word:
        string += letter

    return string


def is_anagram(first_string, second_string):
    letters1 = [letter for letter in first_string.lower()]
    letters2 = [letter for letter in second_string.lower()]
    merge_sort(letters1, 0, len(letters1))
    merge_sort(letters2, 0, len(letters2))
    word1 = get_word(letters1)
    word2 = get_word(letters2)
    bool = word1 == word2

    if word1 == "" and word2 == "":
        bool = False

    return (word1, word2, bool)


# O codigo abaixo é melhor na minha opnião, mas não pude usa-lo:

# def bubble_sort(word):
#     letters = [letter for letter in word.lower()]
#     n = len(letters)

#     for ordered_elements in range(n - 1):
#         for item in range(0, n - 1 - ordered_elements):
#             if letters[item] > letters[item + 1]:
#                 current_element = letters[item]
#                 letters[item] = letters[item + 1]
#                 letters[item + 1] = current_element

#     return get_word(letters)

# def is_anagram(first_string, second_string):
#     word1 = bubble_sort(first_string)
#     word2 = bubble_sort(second_string)
#     bool = word1 == word2

#     if word1 == "" and word2 == "":
#         bool = False

#     return (word1, word2, bool)
