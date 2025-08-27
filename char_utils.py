# char_utils.py

def most_frequent_repeating_char(s: str):
    s = s.lower()
    counts = {}
    for char in s:
        if char.isalpha():  # only letters
            counts[char] = counts.get(char, 0) + 1
    # Filter repeating characters
    repeats = {k: v for k, v in counts.items() if v > 1}
    if not repeats:
        return None, 0
    max_char = max(repeats, key=lambda k: repeats[k])
    return max_char, repeats[max_char]
