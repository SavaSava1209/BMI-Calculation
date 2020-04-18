height = float(input('your heighy in cm :'))
weight = float(input('Your weight in kg : '))
bmi = float(weight / (height / 100) / (height / 100))

if bmi  < 18.5:
    print('Thinness')
elif bmi >= 18.5 and bmi < 24:
	print('Healthy weight')
elif bmi >= 24 and bmi < 27:
	print('Overweight')
elif bmi >= 24 and bmi < 27:
	print('Overweight')
elif bmi >= 27 and bmi < 30:
	print('Obesity')
elif bmi >= 30 and bmi < 35:
	print('Moderate Obesity')
else:
	print('Sever Obesity')