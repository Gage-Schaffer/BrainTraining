"""
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

https://leetcode.com/problems/sort-characters-by-frequency/

"""

input_string = "Aabb"


def frequency_sort(s: str) -> str:
    letters = {}
    output = ""
    for letter in s:
        letter_info = (letter, s.count(letter))
        if letter_info[0] in letters.values():
            continue
        else:
            letters[letter_info[0]] = letter_info[1]
    print(letters)

    v = list(letters.values())
    k = list(letters.keys())
    while len(letters) != 0:
        for i in range(v[v.index(max(v))]):
            output += k[v.index(max(v))]
        letters.pop(k[v.index(max(v))])
        k.pop(v.index(max(v)))
        v.pop(v.index(max(v)))

    return output


print(frequency_sort(input_string))
