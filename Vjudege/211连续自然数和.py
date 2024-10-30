sum = int(input())
i = 0
j = 0
while i < sum/2:
    if (i + j)*(j-i+1)/2 == sum:
        print(i,j)
        j += 1
    elif (i + j)*(j-i+1)/2 < sum:
        j += 1
    elif (i + j)*(j-i+1)/2 > sum:
        i += 1
