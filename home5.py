
bangla1_mark = 100
bangla2_mark = 100
english1_mark = 100
english2_mark = 100
General_math = 100
Highermath = 75
Highermath_practical = 25
Bioligy = 75
Bioligy_practical = 25
Physics = 75
Chemistry = 25
Islamic_Religion = 100
Social_science = 100
Ict = 100
result = (bangla1_mark + bangla2_mark + english1_mark + english2_mark + General_math + Highermath + Highermath_practical + Bioligy + Bioligy_practical + Physics + Chemistry + Islamic_Religion + Social_science + Ict)/16
print(result)
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
