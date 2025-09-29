def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    list_of_chars = {}
    for char in text.lower():
        if char in list_of_chars:
            list_of_chars[char] += 1
        else:
            list_of_chars[char] = 1
    return list_of_chars

