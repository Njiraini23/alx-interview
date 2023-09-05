#!/usr/bin/python3
"""minimal operations"""


def minOperations(n) -> int:
    """Operates two operations in a file copy All and
    Paste given number n. Calculates the fewest number of
    operations needed to result in exactly H characters in the
    file"""
    pasted_chars = 1  # the number of characters in a file
    clipboard = 0  # the H's copied in clipboard
    counter = 0  # number of operations

    while pasted_chars < n:
        # checks whether to copy
        if clipboard == 0:
            # will copy everything
            clipboard = pasted_chars
            # will increase the chars
            counter += 1

        # in case nothing is pasted
        if pasted_chars == 1:
            # pastes the chars
            pasted_chars += clipboard
            # increase the chars
            counter += 1
            # continues to the next
            continue

        remaining = n - pasted_chars  # pastes the remaining chars
        # checks the clipboard to paste. The pasted chars
        # cannot be more than the chars in clipboard
        if remaining < clipboard:
            return 0

        # checks whether the chars are divisible
        if remaining % pasted_chars != 0:
            # paste the chars in clipboard
            pasted_chars += clipboard
            # increases the counter in clipboard
            counter += 1
        else:
            # copies all to clipboard
            clipboard = pasted_chars
            # makes the paste now
            pasted_chars += clipboard
            # increases the operations counter
            counter += 2

        # if the results are acheived
        if pasted_chars == n:
            return counter
        else:
            return 0
