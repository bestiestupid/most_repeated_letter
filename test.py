sentence = input("Enter the string : ")

dic = {}
for i in sentence:
    if dic.get(i) is not None:
        dic[i] += 1
    else:
        dic[i] = 1

lst = sorted(dic.items(), key=lambda kv: kv[1])
x = len(lst) - 1
print("The most repeated element/s  is/are :")
while lst[x][1] >= lst[len(lst)-1][1] and not x < 0:
    print(f"\t\t\t\t\t\t\t\t'{lst[x][0]}'")
    x -= 1
