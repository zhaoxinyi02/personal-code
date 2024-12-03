def kan(n,i):
    if n == 1:
        print(i)
    else:
        i+=1
        return kan(int(n/2),i)
n = int(input())
kan(n,1)