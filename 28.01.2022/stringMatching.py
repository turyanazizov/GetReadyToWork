def contains(text, pattern):
    for i in range(len(text)):
        for j in range(len(pattern)):
            if i + j >= len(text):
                break
            if text[i + j] != pattern[j]:
                break
        else:
            return True
    return False
print(contains('10110100110010111', '001011')) #True
print(contains('It is never too late to have a happy childhood', 'happier')) #False
