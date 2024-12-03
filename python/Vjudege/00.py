data = input()
ltmp = list(data)
ltmp.remove("@")
data = "".join(ltmp)
l = data.split(".")
#l.remove("@")
for i in l:
    try:
        tmp = int(i[:])
        l[l.index(i)] = tmp
    except:
        tmp = list(i[:])
        for j in tmp:
            try:
                tmp2 = int(j[:])
                tmp[tmp.index(j)] = tmp2
            except:
                pass
        l[l.index(i)] = tmp
while len(l) != 1:
    for i in range(len(l)):
        try:
            if l[i][0] == "-":
                tmp = l[i - 2] - l[i - 1]
                l[i - 2] = tmp
                try:
                    del l[i][0]
                except:
                    del l[i]
                del l[i - 1]
                break
            elif l[i][0] == "*":
                tmp = l[i - 2] * l[i - 1]
                l[i - 2] = tmp
                try:
                    del l[i][0]
                except:
                    del l[i]
                del l[i - 1]
                break

            elif l[i][0] == "+":
                tmp = l[i - 2] + l[i - 1]
                l[i - 2] = tmp
                try:
                    del l[i][0]
                except:
                    del l[i]
                del l[i - 1]
                break
            elif l[i][0] == "/":
                tmp = l[i - 2] / l[i - 1]
                l[i - 2] = int(tmp)
                try:
                    del l[i][0]
                except:
                    del l[i]
                del l[i - 1]
                break
        except:
            pass

    for i in range(len(l)):
        try:
            if len(l[i]) == 1:
                l[i] = l[i][:][0]
        except:
            pass

print(l[0])