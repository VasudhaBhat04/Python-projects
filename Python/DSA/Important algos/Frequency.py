# Given a string, find the frequency of each character (how many times each character appears.

def char_frequency(s):
    s=s.lower()  # s = s.lower().replace(" ", "") ignores whitespaces

    freq = {}  # empty dictionary
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

print(char_frequency("Dosa is loved by many"))


# Using collections.Counter
#Counter is a class in the collections module that helps you count how many times each element appears in an iterable (like a list, string, or tuple).
# smart dictionary that automatically does the counting for you.
from collections import Counter

s = "Minions tonight we steal the moon"
freq = Counter(s)
print(freq)

# Count Each Character Individually 

s = "Data structures is difficult"
for ch in set(s):   # set() removes duplicates
    print(ch, ":", s.count(ch))


