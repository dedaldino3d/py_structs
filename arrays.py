###### Arrays ########
import sys
import copy


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, n, start=None, stop=None):
        if not 0 <= n < self._n:
            return IndexError("invalid index")
        if start:
            return self._A[start:]
        if stop:
            return self._A[:stop]
        return self._A[n]

    def append(self, e):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = e
        self._n += 1

    def insert(self, k, v):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[k] = v
        self._n += 1

    def remove(self, v):
        for k in range(self._n):
            if self._A[k] == v:
                for i in range(k, self._n - 1):
                    self._A[i] = self._A[i + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError("value not found")

    def pop(self):
        if self._n > 1:
            self._A[self._n - 1] = None
            self._n -= 1

    def _resize(self, t):
        B = self._make_array(t)
        for k in range(self._n):
            self._A[k] = self._A[k-1]
            B[k] = self._A[k]
        self._A = B
        self._capacity = t

    def _make_array(self, arr):
        return (arr * ctypes.py_object)()


def insertion_sort(A):
    if not isinstance(A, list):
        raise ValueError("invalid, must be an instance of list")
    for k in range(1, len(A)):
        curr = A[k]
        j = k
        while j > 0 and A[j - 1] > curr:
            A[j] = A[j-1]
            j -= 1
        A[j] = curr

####### Caesar cipher #########


class CaesarCipher:
    """Class to perform a caesar cipher encripting and decripting messages"""

    def __init__(self, shift):
        """Construct the caesar cipher using given shift rotation"""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))

        self._forward = ''.join(encoder)  # will store as string
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        """Encrypt message"""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Decrypt message"""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utitlity to perform transformation based on given code string"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]  # replace this character
        return ''.join(msg)


###### Exercies ########

class FullCaesarCipher:

    def __init__(self, shift):
        _encoder = [None] * 3000
        _decoder = [None] * 3000

        for k in range(3000):
            _encoder[k] = chr((k + shift) % 3000 + ord('ל'))
            print(f'key {k} shift-key {k-shift}')
            _decoder[k] = chr((k - shift) % 3000 + ord('ל'))

        self._forward = ''.join(_encoder)
        self._backward = ''.join(_decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            j = ord(msg[k]) - ord('ל')
            msg[k] = code[j]
        return ''.join(msg)


def check_list_size(n):
    data = []
    for d in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(d, b))
        data.append(None)


def check_list_size2(n):
    data = []
    c = sys.getsizeof(data)
    for d in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        c = sys.getsizeof(data[:-1])
        print(c, b)
        if c != b:
            print(f"Lenght: {a-1}")
        data.append(None)


def list_shrink(n):
    data = [None] * n
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Lenght: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.pop()


def find_rep_int(A):
    if not isinstance(A, (list, DynamicArray)):
        raise TypeError("Pass an array in argument, give: ", type(A))


def sum_in_muArray(L):
    """Very poor algorithm (cannot call it as algorithm :(, badless)"""
    sum_i = 0
    for i in L:
        if isinstance(i, list):
            for k in i:
                if isinstance(k, list):
                    for j in k:
                        if isinstance(j, list):
                            for t in j:
                                if isinstance(t, list):
                                    for y in t:
                                        sum_i += y
                                else:
                                    sum_i += t
                        else:
                            sum_i += j
                else:
                    sum_i += k
        else:
            sum_i += i
    return sum_i


def best_sum_in_muArray(L, n):
    if n == 0:
        return 0
    sum_i = 0
    for k in range(n):
        if isinstance(k, list):
            n = len(k)
            return best_sum_in_muArray(k, n-1)
        sum_i += k
    return sum_i




if __name__ == '__main__':
    L = [1, 3, 4, 5, [4, 3, 5, 13, 24], 7, 4, [2, 5, [3953, 5]], 7]
    print(sum_in_muArray(L))
    print(best_sum_in_muArray(L, len(L)))
