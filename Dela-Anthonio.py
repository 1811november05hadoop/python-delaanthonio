#!/usr/bin/env python3

import math
import string
from typing import List


'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''


def main():
    '''
    Use the main function for testing purposes and to show me results for all functions.
    '''
    assert reverse('example') == 'elpmaxe'
    assert acronym('Portable Network Graphics') == 'PNG'
    assert whichTriangle(5.0, 6.0, 7.0) == 'scalene'
    assert whichTriangle(6.0, 5.0, 7.0) == 'scalene'
    assert whichTriangle(5.0, 6.0, 5.0) == 'isosceles'
    assert whichTriangle(5.0, 5.0, 6.0) == 'isosceles'
    assert whichTriangle(6.0, 5.0, 5.0) == 'isosceles'
    assert whichTriangle(5.0, 5.0, 6.0 - 1.0) == 'equilateral'
    assert scrabble('Xanax') == 19
    assert scrabble('Fire') == 7
    assert scrabble('Cabbage') == 14
    assert scrabble('Zip') == 14
    assert scrabble('Muzjiks') == 29
    assert armstrong(153)
    assert not armstrong(154)
    assert primeFactors(48) == [2, 2, 2, 2, 3]
    assert primeFactors(330) == [2, 3, 5, 11]
    assert pangram('The quick brown fox jumps over the lazy dog')
    assert not pangram('The quick brown fox jumped over the lazy dog')
    print(sort([5, 3, 4, 2, 1]))
    print(rotate(13, 'abcdefghijklmnopqrstuvwxyz'))


def reverse(string: str) -> str:
    '''
    1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

    Rules:
    - Do NOT use built-in tools
    - Reverse it your own way
    
    param: str
    return: str
    '''
    return string[::-1]


def acronym(phrase: str) -> str:
    '''
    2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
    Acronyms)! Help generate some jargon by writing a program that converts a
    long name like Portable Network Graphics to its acronym (PNG).
    
    param: str
    return: str
    '''
    words = phrase.split()
    letters = [word[0] for word in words]
    return ''.join(letters)


def whichTriangle(sideOne: float, sideTwo: float, sideThree: float) -> str:
    '''
    3. Determine if a triangle is equilateral, isosceles, or scalene. An
    equilateral triangle has all three sides the same length. An isosceles
    triangle has at least two sides the same length. (It is sometimes specified
    as having exactly two sides the same length, but for the purposes of this
    exercise we'll say at least two.) A scalene triangle has all sides of
    different lengths.
    
    param: float, float, float
    return: str -> 'equilateral', 'isoceles', 'scalene'
    '''
    sides = sorted([sideOne, sideTwo, sideThree])
    if math.isclose(sides[0], sides[2]):
        return 'equilateral'
    if math.isclose(sides[0], sides[1]) or math.isclose(sides[1], sides[2]):
        return 'isosceles'
    return 'scalene'


def scrabble(word: str) -> int:
    '''
    4. Given a word, compute the scrabble score for that word.

    --Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
    C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
    "cabbage" should be scored as worth 14 points:

    3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
    point for E And to total:
    
    3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

    param: str
    return: int
    '''
    score_of = {}
    values = [('aeioulnrst', 1), ('dg', 2), ('bcmp', 3), ('fhvwy', 4), ('k',
                                                                        5),
              ('jx', 8), ('qz', 10)]
    for letters, val in values:
        for char in letters:
            score_of[char] = val
    return sum(score_of[letter] for letter in word.casefold())


def armstrong(number: int) -> bool:
    '''
    5. An Armstrong number is a number that is the sum of its own digits each
    raised to the power of the number of digits.

    For example:
    
    9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
    because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
    5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
    != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
    a number is an Armstrong number.

    param: int
    return: bool
    '''
    digits = [int(x) for x in str(number)]
    digit_count = len(digits)
    return sum(x**digit_count for x in digits) == number


def primeFactors(number: int) -> List[int]:
    '''
    6. Compute the prime factors of a given natural number.

    A prime number is only evenly divisible by itself and 1.

    Note that 1 is not a prime number.
    
    param: int
    return: list
    '''
    x = 1
    factors = []
    while x <= number:
        x += 1
        while number % x == 0:
            factors.append(x)
            number //= x
    return factors


def pangram(sentence: str):
    '''
    7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
    gramma, "every letter") is a sentence using every letter of the alphabet at
    least once. The best known English pangram is:
    
    The quick brown fox jumps over the lazy dog.
    
    The alphabet used consists of ASCII letters a to z, inclusive, and is case
    insensitive. Input will not contain non-ASCII symbols.
    
    param: str
    return: bool
    '''
    letters = set(sentence)
    return all(
        ascii_letter in letters for ascii_letter in string.ascii_lowercase)


def sort(numbers: List[int]) -> List[int]:
    '''
    8. Sort list of integers.
    f([2,4,5,1,3,1]) = [1,1,2,3,4,5]
    
    Rules:
    - Do NOT sort it with .sort() or sorted(list) or any built-in tools.
    - Sort it your own way
    
    param: list
    return: list
    '''
    nums = numbers[:]
    for _ in range(len(numbers)):
        for i in range(1, len(numbers)):
            if nums[i] < nums[i - 1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
    return nums


def rotate(key: int, string: str) -> str:
    '''
    9. Create an implementation of the rotational cipher, also sometimes called
    the Caesar cipher.
    
    The Caesar cipher is a simple shift cipher that relies on transposing all the
    letters in the alphabet using an integer key between 0 and 26. Using a key of
    0 or 26 will always yield the same output due to modular arithmetic. The
    letter is shifted for as many values as the value of the key.
    
    The general notation for rotational ciphers is ROT + <key>. The most commonly
    used rotational cipher is ROT13.

    A ROT13 on the Latin alphabet would be as follows:

    Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
    stronger than the Atbash cipher because it has 27 possible keys, and 25
    usable keys.

    Ciphertext is written out in the same formatting as the input including
    spaces and punctuation.

    Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
    quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
    gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
    quick brown fox jumps over the lazy dog.

    param: int, str
    return: str
    '''
    return string[key:] + string[:key]


def evenAndOdds() -> None:
    '''
    10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
    the odd numbers in a file called odd.txt.
    
    param: none, from the keyboard
    return: nothing
    '''
    with open('odd.txt') as odd, open('even.txt') as even:
        for _ in range(10):
            num = int(input())
            if num % 2 == 0:
                even.write(num)
            else:
                odd.write(num)


if __name__ == "__main__":
    main()
