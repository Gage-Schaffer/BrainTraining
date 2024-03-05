"""
Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

https://leetcode.com/problems/ransom-note/description/

"""

ransom_note = "ba"
magazine = "aabb"


def can_construct(note: str, source: str) -> bool:
    letter_map = {}
    for letter in source:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    for letter in note:
        if letter in letter_map:
            letter_map[letter] -= 1
            if letter_map[letter] < 0:
                return False
        else:
            return False
    return True


print(can_construct(ransom_note, magazine))
