
bangla1_mark = float(input("total bangla1 mark "))
bangla2_mark = float(input("total bangla2 mark "))
english1_mark = float(input("total english1 mark "))
english2_mark = float(input("total english2 mark "))
General_math = float(input("total General_math mark "))
Highermath = float(input("Total Highermath mark "))
Highermath_practical = float(input("Total Highermath_practical mark "))
Bioligy = float(input("Bioligy mark"))
Bioligy_practical = float(input("Total Bioligy_practical mark "))
Physics = float(input("Total Physics mark "))
Chemistry = float(input("Total Chemistry mark "))
Islamic_Religion = float(input("Total Islamic_Religion mark "))
Social_science = float(input("Total Social_science mark "))
Ict = float(input("Total Ict mark "))
result = (bangla1_mark + bangla2_mark + english1_mark + english2_mark + General_math + Highermath + Highermath_practical + Bioligy + Bioligy_practical + Physics + Chemistry + Islamic_Religion + Social_science + Ict)/16
if(result>=80 or result<=100):
    print("your grade is: A+")
    print("your grade is: 5.0")
elif(result>=70 or result<80):
    print("your grade is: A")
    print("your grade is: 4.00")
elif(result>=60 or result<70):
    print("your grade is: A-")
    print("your grade is: 3.5")
elif(result>=50 or result<60):
    print("your grade is: B")
    print("your grade is: 3.00")
elif(result>=40 or result<50):
    print("your grade is: C")
    print("your grade is: 2.0")
elif(result>=33 or result<40):
    print("your grade is: D")
    print("your grade is: 1.0")
else:
    result>=32 or result<00
    print("you are failed: F")
    print("your grade is: 0.0")


