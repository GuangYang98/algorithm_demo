#find the lost possitive interger number in a constant interger list
#initialize the list
li=[3,4,-1,1]

#make negative elements postive, but this will cause mistake
#abs_li = list(map(abs,li))
#print(list(map(abs,li)))

#filter negative elements
filt_li = [elem for elem in li if elem >0]
#print(filt_li)

rank_li = list(set(filt_li))
#print(rank_li)

pare_li = [x for x in range(rank_li[0], rank_li[0]+len(rank_li))]
#print(pare_li)

for i in range(0, len(rank_li)):
    if rank_li[i]!=rank_li[0]+i:
        print(rank_li[0]+i)
        break
