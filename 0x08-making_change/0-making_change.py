#!/usr/bin/python3
""" A pile of coins of different values, determine
the fewest number of coins needed to meet a given
amount total """


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += 1
            temp += 1
        if check == total:
            return temp
        check -= 1
        temp -= 1
    return -1
