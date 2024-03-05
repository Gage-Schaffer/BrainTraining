"""
The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers,
 such as credit card numbers.

 This short program takes an input, cleans it of illegal characters, and then checks the validity of the
 card number. It returns "VALID" for a number that is valid, and "Invalid" otherwise
"""


def clean_input(user_input):
    """
    Takes an input string and removes illegal characters. Returns
    the string as is without the illegal characters

    Parameters
    ------------
    user_input: str

    Returns
    ------------
    cleaned_input: str
    """
    modified_input = user_input
    illegal_chars = [" ", "-", "/"]
    for char in illegal_chars:
        modified_input = modified_input.replace(char, "")

    return modified_input


def check_validity(number_as_str):
    cleaned_input = clean_input(number_as_str)
    l1 = []
    sum = 0
    for idx, i in enumerate(cleaned_input[-2::-2]):
        i = int(i) * 2
        if i > 9:
            i -= 9
        l1.append(i)
    for i in cleaned_input[::-2]:
        l1.append(int(i))

    for numb in l1:
        sum += numb

    if sum % 10 == 0:
        print("VALID CARD")
    else:
        print("INVALID CARD")


card_number = input("Enter your card number: ")
check_validity(card_number)
