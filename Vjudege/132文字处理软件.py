times = int(input())
str = input()
str_list = []

def after_entry(str1,str2):
    str_n = str1+str2
    return str_n

def jiequstr(str,a,b):
    str_n = str[a:a+b]
    return str_n

def charustr(a,str1,str2):
    rstr = str1[:a]
    lstr = str1[a:]
    str_n = rstr + str2 +lstr
    return str_n

def findson(str1,str2):
    try:
        str1_list = list(str1)
        str2_list = list(str2)
        index = str1_list.index(str2_list[0])
        return index
    except ValueError:
        return -1

for i in range(times):
    job = input()
    job_list = job.split(" ")
    job_num = job_list[0]
    if job_num == "1":
        str = after_entry(str,job_list[1])
        str_list.append(str)
    elif job_num == "2":
        str = jiequstr(str,int(job_list[1]),int(job_list[2]))
        str_list.append(str)
    elif job_num == "3":
        str = charustr(int(job_list[1]),str,job_list[2])
        str_list.append(str)
    elif job_num == "4":
        str = findson(str,job_list[1])
        str_list.append(str)
for i in str_list:
    print(i)