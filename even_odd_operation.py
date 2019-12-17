#a N integer list needs to delete all elements one by one from head or tail, needs N steps
#odd step is '-', even is '+' return biggest score
#[2,3,7,10,23,5] sum=50 
#1: score:50, delete 5, sum=45
#2: score:50-45=5, delete 2, sum=43
#3: score:5+43=48......

#___________
#BFS transfer all array to the next state-->slow and outofmemory
#___________

#!/bin/python3

import math
import os
import random
import re
import sys

def getMaximumScore(integerArray):
    # Write your code here
    '''n = len(integerArray)
    queue = []
    visited = [[0] * n for i in range(n)]
    score = 0
    i = 0
    start = 0
    end = len(integerArray) - 1
    #queue.append((integerArray, sum(integerArray), score,i))

    queue.append((start, end, sum(integerArray), score,i))

    maxscore = 0
    while queue:
        s = queue.pop(0)
        start, end, summ, score, i = s
        if (summ == 0):
            if score > maxscore:
                maxscore = score
        else:
            if (visited[start][end] > score):
                continue
            visited[start][end] = score
            i += 1 
            if i%2==0:
                score = score - summ
            else:
                score = score + summ
            sleft = (start+1, end,summ-integerArray[start],score, i)
            sright = (start, end-1, summ-integerArray[end],score, i)
            queue.append(sleft)
            queue.append(sright)
    return maxscore'''

    g = [0]
    summ = 0
    #sum(arr[i:j])=g[j] - g[i]
    for x in integerArray:
        summ += x
        g.append(summ)
    
    n = len(integerArray)
    dp = [[0] * n for i in range(n)]
    for length in range(n-1, 0, -1):
        for st in range(n-length+1):
            end = st + length - 1
            step = n - length
            if (st == 0):
                if (step%2==0):
                    dp[st][end] = dp[st][end+1] - (g[end+2]-g[st])
                else:
                    dp[st][end] = dp[st][end+1] + (g[end+2]-g[st])
            elif (end == n-1):
                if (step%2==0):
                    dp[st][end] = dp[st-1][end] - (g[end+1]-g[st-1])
                else:
                    dp[st][end] = dp[st-1][end] + (g[end+1]-g[st-1])
            else:
                if (step%2==0):
                    dp[st][end] = max(
                        dp[st][end+1] - (g[end+2]-g[st]),
                        dp[st-1][end] - (g[end+1]-g[st-1])
                    )
                else:
                    dp[st][end] = max(
                        dp[st][end+1] + (g[end+2]-g[st]),
                        dp[st-1][end] + (g[end+1]-g[st-1])
                    )
    maxscore = 0
    step = n
    for st in range(n):
        if (step%2==0):
            dp[st][st]-=integerArray[st]
        else:
            dp[st][st]+=integerArray[st]
        if (dp[st][st] > maxscore):
            maxscore = dp[st][st]
    print(integerArray)
    print(g)
    print(dp)
    return maxscore
