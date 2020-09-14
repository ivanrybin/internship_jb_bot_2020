
from top_words.words_handler import find_top_words, pretty_print

if __name__ == '__main__':
    words_any_case, words_lower_case = find_top_words()

    print('Слова без учета регистра')
    pretty_print(words_any_case)

    print('\nСлова с приведением к нижнему регистру')
    pretty_print(words_lower_case)
