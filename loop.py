name = input("enter your name: ")
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    print(asc)
    sum = sum + asc
print(sum)

