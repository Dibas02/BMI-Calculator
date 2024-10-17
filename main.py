weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in mtr: "))

bmi = weight/height**2

if bmi<18.5 :
    print("You are underweight")

elif bmi<25 : 
    print("You are healthy")

elif bmi<30:
    print("You are overweight")

elif bmi<35:
    print("You are severly overweight")

else:
    print("You are obessed")
