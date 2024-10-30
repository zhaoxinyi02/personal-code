print("欢迎来到王者荣耀")
name = input("请输入英雄名")
print("好的",name)
xingbie = input("请输入性别")
print("好的",name)
nianling = int(input("请输入年龄"))
zhiye = int(input("请选择您的职业. 1.战士 2.坦克 3.法师 4.射手 5.辅助"))
zhiye -= 1
tf = input("是否需要合作伙伴")


zhiyelist = ["战士","坦克","法师","射手","辅助",]

if xingbie == "男":
    xingbie1 = "勇士"
elif xingbie == "女":
    xingbie1 = "女神"

if nianling <= 20:
    chenghu = "少年英雄"
elif nianling > 20:
    chenghu = "老江湖"

zhiye1 = zhiyelist[zhiye]

if tf == "是":
    print("欢迎您,",nianling,"的",name,xingbie1,"您选择的职业是；",zhiye1,",您不需要合作伙伴",",您真是个",chenghu)
elif tf =="否":
    print("欢迎您,",nianling,"的",name,xingbie1,"您选择的职业是；",zhiye1,",您需要合作伙伴",",您真是个",chenghu)










