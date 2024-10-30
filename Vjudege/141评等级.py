exlist=[]
n=int(input())
for i in range(0,n):
    nums=input()
    xueye=int(nums.split(' ')[1])
    suzhi=int(nums.split(' ')[2])
    if xueye+suzhi>140 and xueye*7 + suzhi*3>=800:
        exlist.append('Excellent')
    else:
        exlist.append('Not excellent')
for i in exlist:
    print(i)
