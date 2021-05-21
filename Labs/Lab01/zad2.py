import numpy as np


def createDic(m, n):
    dic = {}
    for i in range(m, n+1):
        dic[i] = (i*i, np.power(i, 3), np.sqrt(i))

    return dic

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    #vasiot kod pisuvajte go tuka

    rng = {}
    if n > m:
        rng = createDic(m, n)
    if x in range(m, n+1):
        print(rng[x])
    else:
        print("nema podatoci")
    print(rng)