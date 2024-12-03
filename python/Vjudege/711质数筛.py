n=int(input())
nums=input()

numlist = []

def tf(n):
    if n == 1:
        return False
    for a in range(2,n):
        if n%a==0:
            return False
    return True

for i in nums.split(' '):
    i = int(i)
    if tf(i):
        numlist.append(i)
for i in numlist:
    print(i,end=' ')
        
    
    
    
