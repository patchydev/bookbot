def count_words(words: str) -> int:
    return len(words.split())
    
def count_chars(words: str) -> dict:
    chars = {}
    
    for c in words:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    return chars
    
def sort_dict(dict: dict) -> list:
    dicts = []
    
    for k, v in dict.items():
        dicts.append({"char": k, "num": v})
    dicts.sort(key=lambda x: x["num"], reverse=True)
    return dicts