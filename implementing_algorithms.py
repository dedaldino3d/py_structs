import ctypes
import sys
import math
import copy
import os
from time import time, sleep


oldRecLimit = sys.getrecursionlimit()
sys.setrecursionlimit(1000000)

# print("Old recursion limit - ", oldRecLimit)

###### Recursion ########


def bad_fibonacci(n):
    """
    This algorithnm run in worst-case O(2^n) - Exponential
    """
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


def good_fibonacci(n):
    """
    This algorithnm run in worst-case O(n) - Linear
    """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)


def linear_sum(S):
    """Summing the elements of a sequence recursively"""
    n = len(S)

    def linear_sum3(S, n):
        if n == 0:
            return 0
        else:
            return linear_sum3(S, n-1) + S[n-1]
    return linear_sum3(S, n)


def find_max(S):
    """Find maximum element in a sequence recursively (Bad)"""

    if not isinstance(S, (list, tuple)):
        return TypeError("S need to be either list or tuple")
    n = len(S)

    def find_max2(S, n):
        max = S[n-1]
        if max > S[n-2]:
            return max
        return find_max2(S, n-1)
    return find_max2(S, n)


def find_max3(S, n):
    """Find maximum element in a sequence recursively (Best)"""
    if n == 0:
        return n
    nmax = S[n-1]
    nprev = S[n-1]
    max = find_max3(S, n-1)
    if nmax > nprev and nmax > max:
        return nmax
    elif nmax > max:
        return nmax
    else:
        return max


def power(x, n):
    '''Compute the power of n'''
    if n == 0:
        return 1
    else:
        partial = power(x, (n)//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def isabel_sum(A):
    A = [power(n, 2) for n in A]
    # create new sequence o A with his half of size
    B = A[:len(A)//2]
    i = (n/2) - 1
    B[i] = A[2*i] + A[2*i + 1]
    if len(B) == 1:
        return B[0]
    return isabel_sum(B)


def is_odd(n):
    return (n // 2) == 0


def isabel_sum2(A, tam):
    B = A[:tam//2]
    for n in A:
        if n**(1/2) % 2 == 0:
            for i in range(len(A)):
                B[i] = A[:len(A)//2]
                i = (n/2) - 1
                B[i] = A[2*i] + A[2*i + 1]
                print("B: ", B)
        else:
            print("No match", end=" ")
    if len(B) == 1:
        return B[0]
    else:
        return isabel_sum2(B, (n/2) - 1)


def min_and_max(S, n):
    if n == 0:
        return (n, 0)
    nmax = S[n-1]
    nmin = S[n-1]
    (minimum, maximum) = min_and_max(S, n-1)
    if nmax > nmin and nmax > maximum and nmin < minimum:
        return (nmin, nmax)
    elif nmax > maximum and minimum < nmin:
        return (minimum, nmax)
    elif maximum > nmax and nmin < minimum:
        return (nmin, maximum)
    else:
        return (minimum, maximum)


def find_product_with_add_sub(m, n):
    if n == 0:
        return (m, n)
    else:
        (m, pm) = find_product_with_add_sub(m, n-1)
        pm += m
        return (m, pm)


def tower_hanoi(n, ini, dest, tmp):
    # Implement this algorithm
    if n > 0:
        print(f"Tower of Hanoi, movs , from {ini} to {dest} using {tmp}")
        tower_hanoi(n-1, dest, tmp, ini)
        print(f"Tower of Hanoi, movs , from {ini} to {dest} using {tmp}")
        tower_hanoi(n-1, tmp, ini, dest)


def reverse_string(S, start, stop):
    if start < stop:
        S = list(S)
        S[start], S[stop - 1] = S[stop - 1], S[start]
        return reverse_string(S, start + 1, stop - 1)
    return "".join(S)


# def is_palindrome(S, revS, start, stop):
#     # Finish this algorithm
#     revS = list(reverse_string(S, 0, len(S))
#     if start < stop:
#         S = list(S)
#         (rev, S) = is_palindrome(S, revS, start + 1, stop - 1)
#         print(rev, S)
#         if rev == S:
#             return True
#         return (rev, S)
#     return False


def more_vowels_than_consonants(S, start, stop):
    # Finish this algorithm
    if start >= stop:
        return (v, c)
    vowels = 'BCDFGHJKLMNPQRSTVWXYZ'
    consonants = 'AEIOU'
    (v, c) = more_vowels_than_consonants(S, start + 1, stop - 1)
    if S[start].upper() in vowels:
        v += 1
        return (v, c,)
    elif S[start].upper() in consonants:
        c += 1
        return (v, c,)
    else:
        return (v, c)


def rearrange(S, start, end, k):
    # Finish algorithm
    if start < end:
        return (S, S)
    (mini, maxi) = rearrange(S, start + 1, end - 1, k)
    if S[start] <= k:
        # S[start], S[end - 1] = S[end - 1], S[start]
        S.pop(start)
        mini.append(S[start])
        return (mini, maxi)
    elif S[start] >= k:
        S.pop(start)
        # S[end - 1], S[start] = S[start], S[end - 1]
        maxi.append(S[start])
        return (mini, maxi)
    else:
        return mini.append(maxi)


def walk(path):
    if os.path.isdir(path):
        dirpath = os.path.dirname(os.path.abspath(path))
        dirnames = []
        filenames = []
        for p in os.listdir():
            if os.path.isdir(p):
                dirnames.append(p)
            elif os.path.isfile(p):
                filenames.append(p)
            yield (path, dirnames, filenames,)

        # for d in dirnames:
        #     yield walk(os.path.join(path, d))


if __name__ == "__main__":
    # Computing fibonacci
    # i1 = time()µ
    # b = bad_fibonacci(40)
    # print(b)
    # f1 = time()
    # i2 = time()
    # g = good_fibonacci(40)
    # print(g)
    # f2 = time()
    # print("Bad Fibonacci time - %ss" %(f1 - i1))
    # print("Good Fibonacci time - %ss" %(f2 - i2))
    # Computing linear sum
    S = [i for i in range(1000)]
    # print(linear_sum(S))
    # max = find_max(S)
    # print(max)
    # Computing maximum element
    # i1 = time()
    # max1 = find_max(S)
    # print(max1)
    # f1 = time()
    # i2 = time()
    a = [3, 5, 3, 6, 35, 4, 6, 63, 7, 3673, 8,
         36, 3, 8, 3, 5434, 163, 3, 7, 3889, 674]
    # max2 = find_max3(a, len(a))
    # print(max2)
    # f2 = time()
    # e1 = f1 - i1
    # e2 = f2 - i2
    # print("Find max 1 time - %ss" %e1)
    # print("Find max 3 time - %ss" %e2)
    # st = "123456789"
    # print(convert_str2int(st, len(st)))
    # Computing isabel_sum
    # isb = isabel_sum2(S)
    # print(isb)
    # Computing minimum and maximum value in a sequence
    # min_max = min_and_max(a, len(a))
    # print(min_max)
    # Computing minimum and maximum value in a sequence
    # print(find_product_with_add_sub(2,2))
    # Computing reverse string
    # s = "pata"
    # revs = reverse_string(s, 0, len(s))
    # print(revs)
    # Computing is_palindrome
    # pali = "dedaldino"
    # print(is_palindrome(pali, pali, 0,len(pali)))
    # Computing vowels than consonants
    # print(more_vowels_than_consonants(pali, 0, len(pali)))
    # Computing rearrange elements in a sequence
    # print(rearrange(a, 0, len(a), 100))
    # Computing walk like os.walk
    # for r,d,f in walk(os.path.abspath('.')):
    #     print(r, d, f)
    # Computing tower_hanoi
    # tower_hanoi(3, 'A', 'B', 'C')
    # Computing criptography with Caesar cipher
    cipher = CaesarCipher(4)
    message = "DEDALDINO the eagle is IN play; meet at joe's."
    coded = cipher.encrypt(message)
    print(coded)
    decr = cipher.decrypt(coded)
    print(decr)
