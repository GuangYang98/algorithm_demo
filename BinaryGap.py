#1.transfer the integer N to binary
#2.find the biggest continuing '0' between two '1's 

def solution(N):
    # write your code in Python 3.6
    result = []
    n=N
    while n != 0:
        result.insert(0,n%2)
        n=n//2
    re = 0
    big = 0
    for i in result:
        if i ==1:
            if big <= re:
                big = re
            re=0
        else:
            re = re+1
            
    return big
    pass
