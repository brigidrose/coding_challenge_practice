"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    output = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            output.append(i)
    return output


###############################################################################

"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    seen = {}  #create empty dictionary to store letters seen in it.

    #count each letter

    for letter in word:
        #looks for key. if key isnt there, set new key to zero
        count = seen.get(letter, 0) #.get returns all keys that are equal. Add a default value (the 0) in case that key doesn't yet exist in dict
        #dict[the current key we are looking at] = add the current val by 1
        seen[letter] = count + 1

    #new var setting odd nums seen to zero
    seen_an_odd = False

    # look at each value in the seen dict
    for count in seen.values():
        # if the current val is not divisible by 2
        if count % 2 != 0:
            #until you have seen your first odd number it remains false
            if seen_an_odd:
                return False
            #when you've seen your first even number, it turns true
            seen_an_odd = True

    return True

###############################################################################






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EVENLY HANDLED! WAY TO CRUSH IT!\n"
