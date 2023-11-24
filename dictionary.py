# car = {"model":"ml","color":"red","price":100}
# print(car['price'])
# print(car.get('model'))
# print(car.keys())
# print(car.values())

# for i in car:
#     print(i)
# for i in car.values():
#     print(i)
# for i,j in car.items():
#     print(i,j)
cars = {"car1":
        {"model":"ml","price":100},
         "car2":
         {"model":"m2","price":1000}}
for i,j in cars.items():
    for k in j.items():
        print(i,k)