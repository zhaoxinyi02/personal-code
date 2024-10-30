from re import findall
s = input()
resulta = findall(r'a:=(.);',s)
resultb = findall(r'b:=(.);',s)
resultc = findall(r'c:=(.);',s)
list = []
#print(result)
for i in resulta:
    try:
        i = int(i)
        list.append(i)
    except ValueError:
        list.append(0)

for i in resultb:
    try:
        i = int(i)
        list.append(i)
    except ValueError:
        list.append(0)

for i in resultc:
    try:
        i = int(i)
        list.append(i)
    except ValueError:
        list.append(0)
for i in list:
    print(i,end=" ")