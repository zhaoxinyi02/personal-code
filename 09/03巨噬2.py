begin = 26
for i in range(100):
    end = begin*pow(2,i)
    if end+1 > 100000:
        print(i)
        break