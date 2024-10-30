n = int(input())
l2 = [[1], [1, 1]]
for i in range(2, n):
    before = l2[i-1]
    present = []
    present.append(1)   #头
    for j in range(i-1):
        present.append(before[j]+before[j+1])
    present.append(1)   #尾
    l2.append(present)
for i in range(n):
    s = "  "*(n-i-1)
    for j in l2[i]:
        if len(str(j)) == 1:
            s = s + str(j)+"   "
        elif len(str(j)) == 2:
            s = s + str(j) + "  "
        elif len(str(j)) == 3:
            s = s + str(j) + " "
    print(s)
input()