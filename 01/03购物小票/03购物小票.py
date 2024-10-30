import datetime



namelist = []      #为每个数据创建一个列表
pricelist = []
numberlist = []
tpricelist = []


kuantai = input("请输入款台：")
shouyinyuan = input("请输入收银员号：")


while True:
    name = input("请输入商品名称：")
    namelist.append(name)
    price = input("请输入单价：")
    price = int(price)
    pricelist.append(price)
    number = input("请输入数量：")
    number = int(number)
    numberlist.append(number)

    tf = input("是否继续,输入no以结算,否则回车继续")      #判断是否终止循环


    if tf == "no":
        t = datetime.datetime.now()
        t = t.replace(microsecond = 0)
        print("         XXX超市（欢迎光临）\n")
        print("款台："+kuantai+"   "+"收银员号："+shouyinyuan+"\n")
        print("日期：",t)
        print("-------------------------------------\n")
        print("商品名      单价     数量     金额\n")

        longth = len(namelist)
#        longth = longth + 1
#        print(type(longth))
        for i in range(0,longth):
#            print(i)
#            a = pricelist[i]
#            print(type(a))
#            print(pricelist[i])
#            print(numberlist[i])
            a = int(pricelist[i])
            b = int(numberlist[i])
            tprice = a*b
            tpricelist.append(tprice)     #添加每个商品的总价
            n = str(namelist[i])
            p = str(pricelist[i])
            n2 = str(numberlist[i])
            t = str(tpricelist[i])

            print(n+"    "+"      "+p+"      "+n2+"       "+t)
            
        totalprice = 0          #以下开始计算总价以及找零
        for x in tpricelist:
            totalprice += x
        totalprice = str(totalprice)
        print("-------------付款方式如下------------")
        print("应付："+totalprice)
        totalprice = int(totalprice)
        money = int(input("实收："))
        cash = money - totalprice
        print("找零：",cash)
        
        
    else:
        continue

    break

input()       #防止输出小票完毕窗口一闪而过