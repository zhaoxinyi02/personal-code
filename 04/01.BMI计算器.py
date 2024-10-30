

print("欢迎来到肥胖计算器")
while True:

    weight = float(input("请输入你的体重 （单位：kg）"))
    hight = float(input("请输入你的身高 （单位：m）"))
    hight_2 = hight**2
    BMI = weight/hight_2
    print("你的BMI是：",BMI)
    tf = input("请问是否还要玩一遍？t or f")
    if tf == "t":
        continue
    elif tf == "f":
        print("欢迎下次在玩，拜拜！")
        break
