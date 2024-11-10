class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                result = file.read().lower()
                for need_remove in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    result = result.replace(need_remove, '')
                words = result.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        pos = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                pos[name] = words.index(word) + 1
        return pos

    def count(self, word):
        word = word.lower()
        count = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            times = 0
            for words_ in words:
                if word == words_:
                    times += 1
                    count[name] = times
        return count

# Пример выполнения программы:

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
