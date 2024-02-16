"""

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.


https://leetcode.com/problems/isomorphic-strings/description/

"""

s1 = "title"
t1 = "paper"


def is_isomorphic(s: str, t: str) -> bool:
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:                                  # Check string length and exit if they do not match
        return False

    hash = {}
    for letter_idx in range(s_len):
        if s[letter_idx] in hash.keys():                # If the letter already exists in the hashmap
            if hash[s[letter_idx]] == t[letter_idx]:    # Check if the currently iterated letter matches...
                continue
            else:
                return False                            # ... and return false if it does not
        else:
            hash[s[letter_idx]] = t[letter_idx]         # If the letter does not exist, append it

    return True


print(is_isomorphic(s1, t1))