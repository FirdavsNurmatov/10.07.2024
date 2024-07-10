lst = []
n = int(input('list uzunligi = '))
for i in range(n) :
    lst.append(int(input('n=')))
lst2 = []
for i in range(1,len(lst)) :
    lst2.append(lst[i] - lst[i-1])
print(max(lst2))