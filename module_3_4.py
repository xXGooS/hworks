def single_root_words(root_word, *other_words):
    same_words = []
    switched_root = root_word.lower()
    for word in other_words:
        switched_word = word.lower()
        if switched_word in switched_root or switched_root in switched_word:
            same_words.append(word)

    return same_words

# Пример результата выполнения программы:

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)