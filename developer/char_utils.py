def most_frequent_repeating_char(s):
    s = s.lower()  # case-insensitive
    counts = {}
    for c in s:
        if c.isalpha():  # count letters only
            counts[c] = counts.get(c, 0) + 1
    # filter only repeating chars
    repeats = {k: v for k, v in counts.items() if v > 1}
    if not repeats:
        return {}, None
    # most frequent
    most_frequent = max(repeats.items(), key=lambda x: x[1])
    return repeats, most_frequent
