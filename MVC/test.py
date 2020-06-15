f=open("../Data/datacus.txt", "r", encoding="utf-8")
a=f.readlines()
f.close()
b=list()
c="1800"
for i in a:
    if c in i:
        b.append(i)
        break
if c not in i:
    print("Fales")
print(a)
print(b)