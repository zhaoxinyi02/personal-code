name_list = ["形势与政治1","中国近代史纲要","大学英语（上）","大学英语听说（上）","计算机学科概论","体育（1）","军事理论","高等数学B（上）"]
source_list = []
dot_list = []
study_source_list = [0.5,2.5,5,2,2,1,2,4]
dot_and_study_source_list = []
GPA1_list = []

print("此GPA计算器为百分制计算器")
name = input("请输入你的名字")

for i in name_list:
    print(i)

n = 1
while n <= 8:

    source = int(input("请依次输入分数"))
    source_list.append(source)
    n += 1

for i in range(0,len(name_list)):
    source_2 = source_list[i]
    if source_2 <= 60:
        dot = 0

    else:
        source_3 = source_2 - 60
        dot_3 = source_3 * 0.1
        dot = 1 + dot_3

    dot_list.append(dot)

dot_list2 = dot_list[:]
study_source_list2 = study_source_list[:]
n = 1
while n <= 8:
    d1 = dot_list2[0]
    s1 = study_source_list2[0]
    gpa1 = d1 * s1
    GPA1_list.append(gpa1)
    del dot_list2[0]
    del study_source_list2[0]

    n += 1


GPA2 = 0
for i in GPA1_list:
    GPA2 += i

study_source = 0
for i in study_source_list:
    study_source += i


GPA = GPA2/study_source
print(name,"你的学分是：",round(GPA,2))


