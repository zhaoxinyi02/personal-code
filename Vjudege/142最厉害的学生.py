n=int(input())
students=[]
source=[]
for i in range(0,n):
    s=input()
    student=list(s.split(' '))
    students.append(student)
    n1=int(student[1])
    n2=int(student[2])
    n3=int(student[3])
    source.append(n1+n2+n3)
source2=source[:]
source2.sort()
high=source2[len(source)-1]
index=source.index(high)
for i in students[index]:
    print(i,end=' ')


    
