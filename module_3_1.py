calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Пример результата выполнения программы:

print(string_info('Capybara')) # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon')) # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # True
print(is_contains('cycle', ['recycling', 'cyclic'])) # False
print(calls) # 4
