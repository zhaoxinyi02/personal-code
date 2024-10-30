def func1(s,t):
    if t == 0:
        return
    print(s[t-1],end='')
    func1(s,t-2)
s = input()
l = len(s)
func1(s,l)