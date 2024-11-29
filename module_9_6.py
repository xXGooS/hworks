def all_variants(text):
    len_text = len(text)
    for size in range(1, len_text + 1):
        for i in range(len_text - size + 1):
            yield text[i:i + size]

a = all_variants("abc")
for i in a:
    print(i)