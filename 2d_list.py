# list_2 = [[1,2,3],[4,5,6],[6,7,8]]
# print(list_2[2][2])

# list_1 = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(list_2))

# list_3 = [[1,2,3],[4,5,6],[7,8,9]]
# print(list_3[1])

# list_4 = [[1,2,3],[4,5,6],[7,8,9,10]]
# print(len(list_4[2]))

list_5 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# for i in range(5):
#     for j in range(5):
#         print(i,j)
num_of_rows = len(list_5)
for i in range(num_of_rows):
    col_size = len(list_5[i])
    for col in range(col_size):
        print(list_5[i][col])
