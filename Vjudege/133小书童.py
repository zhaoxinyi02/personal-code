words = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = int(input())
password = input()
password_list = list(password)
password_listn = []
for i in range(len(password_list)):
    zimu = password_list[i]
    index = words.index(zimu)
    inew = words[index + n]
    password_listn.append(inew)
for i in password_listn:
    print(i,end="")
