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

def build_sorted_char_list(list_of_chars):
    items = []
    for ch, n in list_of_chars.items():
        items.append({"char": ch, "num": n})
    
    def sort_on(item):
        return item["num"]
    items.sort(key=sort_on,reverse=True)
    return items