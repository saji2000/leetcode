#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    # print(logs)
    # print(maxSpan)
    sign_in = {}
    sign_out = {}
    ids = set()


    for log in logs:
        info = log.split(" ")
        # print(info)
        id = info[0]
        timestamp = info[1]
        if info[2] == "sign-in":
            sign_in[id] = timestamp
        else:
            sign_out[id] = timestamp
        ids.add(id)


    # print(sign_in, sign_out)
    result = []

    for id in ids:
        if id in sign_in and id in sign_out:
            delta = int(sign_out[id]) - int(sign_in[id])
            if delta <= maxSpan:
                result.append(id)
    # print(result)
    
    return sorted(result)
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

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
