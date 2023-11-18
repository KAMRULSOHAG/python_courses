# list_1 = [1,2,3,4,5]
# print(list_1)
# list_1 = [1,2,3,4,5]
# print(len(list_1))
# list_1 = [1,2,3,4,5]
# print(list_1[0])
# list_1 = [1,2,3,4,5]
# print(list_1[0:3])
# list_1 = [10,21,33,40,50,50]
# for i in range(len(list_1)):
#     print(i,list_1[i])

# sum = 0

# appent - add the value into last index
# print("before append",list_1)
# list_1.append(60)
# print("aftet append",list_1)

# clear = clear the all elements in a list
# list_1.clear()
# print("after clear",list_1)
# copy() = copy of list to another
# list_2 = list_1.copy()

# print("after copy",list_2)

# cnt = list_1.count(50)

# count = 0
# for i in list_1:
#     if(i==50):
#         count = count+1
#     else:
#         count = count
# print(count)
# for i in list_1:
#     sum = sum + i
# print(sum)

# even_list =[]
# odd_list = []



# for i in list_1:
#     if(i%2==0):
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(even_list)
# print(odd_list)

# list_1.insert(0,100)
# print("after insert",list_1)

# pop (), remove(), sort(), indx(), extend()


# name = input("enter your name: ")
# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     print(i,asc)
#     sum = sum + asc
# print(sum)

name_1 = ("ab,cd,ef")
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    print(i,asc)
    sum = sum + asc
print(sum)
name_2 = name_1.copy()
print("after copy",name_2)


