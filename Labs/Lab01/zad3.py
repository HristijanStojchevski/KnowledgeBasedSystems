import numpy as np


def createDic(m, n):
    dic = {}
    for i in range(m, n+1):
        dic[np.power(i, 3)] = i
    return dic


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    #vasiot kod pisuvajte go tuka

    rng = {}
    if n > m:
        rng = createDic(m, n)
        if x in rng.keys():
            print(rng[x])
        else:
            print("nema podatoci")
    else:
        print("nema podatoci")
    print(rng)