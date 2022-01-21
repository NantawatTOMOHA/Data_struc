

print(" *** BMI ***")
data = (input('Enter your weight(kg) and height(m) : ').split())
x=float(data[0])
y=float(data[1])



Bmi=x/(y*y)

if Bmi<18.5 :
    print("Your status is : Below normal weight.")
elif Bmi >= 18.5 and  Bmi < 25 :
    print("Your status is : Normal weight.")
elif Bmi >= 25 and Bmi <30 :
    print("Your status is : Overweight.")
elif Bmi >= 30 and Bmi <35 :
    print("Your status is : Case I Obesity.")
elif Bmi >= 35 and Bmi <40 :
    print("Your status is : Case II Obesity.")
elif Bmi >= 40 :
    print("Your status is : Case III Obesity.")


