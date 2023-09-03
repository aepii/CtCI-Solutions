# 1.1 Is Unique:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def isUnique(string: str) -> bool:

    if len(string) > 128: return False

    char_set = [False for n in range(128)]

    for letter in string:
        val = ord(letter)

        if char_set[val]:
            return False

        char_set[val] = True

    return True


print(isUnique("0abcABC"))
