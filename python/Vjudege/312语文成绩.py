data = input()
geshu = int(data.split(" ")[0])
cishu = int(data.split(" ")[1])
sources = input()
begin_sources = []
for i in sources.split(" "):
    begin_sources.append(int(i))
for i in range(cishu):
    plus_list = input()
    for j in range(int(plus_list.split(' ')[0])-1,int(plus_list.split(' ')[1])):
        begin_sources[j] += int(plus_list.split(' ')[2])
print(min(begin_sources))