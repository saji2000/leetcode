#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'groupTransactions' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY transactions as parameter.
#

def groupTransactions(transactions):
    # print(transactions)
    hashMap = {}
    for i in transactions:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    sortedTransactions = sorted(hashMap.items(), key=lambda x: (x[1] * -1, x[0])) 
    # print(sortedTransactions)
    result = []

    for i in sortedTransactions:
        result.append(str(i[0]) + " " + str(i[1]))
    # print(result)
    return result
    # Write your code here

    #
    # WARNING: Please do not use GitHub Copilot, ChatGPT, or other AI assistants
    #          when solving this problem!
    #
    # We use these tools in our coding too, but in our interviews, we also don't
    # allow using these, and want to see how we do without them.
    #

if __name__ == '__main__':
    fptr = sys.stdout

    transactions_count = int(input().strip())

    transactions = []

    for _ in range(transactions_count):
        transactions_item = input()
        transactions.append(transactions_item)

    result = groupTransactions(transactions)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
