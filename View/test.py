b = ["45 ", "42 ", "52 ", "49 ", "47"]
f=open("feedback.txt","a",encoding="utf-8")
for i in b:
    f.write(i)
f.close()
g=open("feedback.txt","r",encoding="utf-8")
a=g.read().split(" ")
c=list()
for i in a:
    c.append(int(i))
print(c)