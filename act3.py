height = float(input("enter your height in cm:"))
weight = float(input("enter your weight in kg:"))

bmi = weight / (height/100)**2

print("your bmi is", bmi)

if bmi <= 18.4:
    print("your  are underweight.")
elif bmi <= 24.9:
    print("your are healthy.")
elif bmi <= 29.9:
    print("your are over weight.")
elif bmi <= 34.9:
    print("your are severely over weight.")
elif bmi <= 39.9:
    print("your are obese.")
else:
    print("your are  severely obese.")