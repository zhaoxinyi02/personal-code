from random import *
def create_paiku():
    paimian = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    huase = ['黑桃','红心','方块','梅花']
    paiku = []
    for i in paimian:
        tmp = []
        for j in huase:
            tmp.append(j+i)
        paiku.append(tmp)
    paiku.append(['大王','小王'])
    return paiku
    #print(paiku)

def send_pai(paiku,list,num):
    for i in range(num):

        while True:
            cpaishu = choice(paiku)

            if cpaishu == []:
                continue
            chuase = choice(cpaishu)
            list.append(chuase)
            cpaishu.remove(chuase)
            break
    #print(dizhu)

def main():
    paiku = create_paiku()
    dizhu = []
    nongming1 = []
    nongming2 = []
    send_pai(paiku,dizhu,20)
    send_pai(paiku,nongming1, 17)
    send_pai(paiku,nongming2, 17)
    print(dizhu)
    print(nongming1)
    print(nongming2)

if __name__ == "__main__":
    main()