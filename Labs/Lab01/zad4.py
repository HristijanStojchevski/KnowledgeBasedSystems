import numpy as np


if __name__ == '__main__':
    l = list(map(int, input().split(' ')))
    k = int(input())
    # vashiot kod pishuvajte go tuka
    lst = []

    if k >= 0:
        if k > len(l):
            k = k - len(l)
        tmp = l[0:k]
        lst = l[k:] + tmp
    else:
        if -k > len(l):
            k = (abs(k) - len(l)) * (-1)
        tmp = l[k:]
        lst = tmp + l[0:k]
    print(lst)
