name1 = input("Enter your name here: ")
name2 = input("Enter their name here: ")
com = name1 + name2
lo = com.lower()
t = lo.count("t")
r = lo.count("r")
u = lo.count("u")
e = lo.count("e")
true = t + r + u + e
l = lo.count("l")
o = lo.count("o")
v = lo.count("v")
e = lo.count("e")
love = l + o + v + e
comb = str(true) + str(love)
print(comb)
if comb<10 or comb>90:
    print("   ")