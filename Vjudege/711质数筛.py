n=int(input())
nums=input()
numlist=[]
for i in range(n):
    num=int(nums.split(' ')[i])
for i in numlist:
    for a in range(2,i):
        if i%a==0:
            numlist.remove(i)
            break
for i in numlist:
    print(i,end=' ')
        
    
    
    
