#Exercise 1/2/3
my_age = 28
my_height = 1.67
complex_num = 3j

#Exercise 4
b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))
area = 0.5 * b * h
print(f"The area of the triangle is: {area}")

#Exercise 5
a=float(input("Enter side a of the triangle: "))
b=float(input("Enter side b of the triangle: "))
c=float(input("Enter side c of the triangle: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is: {perimeter}")

#Exercise 6
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")

#Exercise 7
r=float(input("Enter the radius of the circle: "))
pi=3.14
area = pi * r**2
circumference = 2 * pi * r
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")

#Exercise 8
# y = 2x - 2
# General form: y = mx + c
m = 2
c = -2
print(f"The slope (m) of the line is: {m}")
# y = 2 * 0(x) - 2
# x = 0, y = -2
y_intercept = m * 0 + c
print(f"The y-intercept (c) of the line is: (0, {y_intercept})")
# 0 = mx + c
# x = -c/m
x_intercept = -c / m
print(f"The x-intercept of the line is: ({x_intercept}, 0)") 

#Exercise 9
#m = y2-y1/x2-x1
#between point (2, 2) and point (6,10)
m = (10 - 2) / (6 - 2)
print(f"The slope of the line between points (2, 2) and (6, 10) is: {m}")

#Exercise 10
task8_slope = 2
task9_slope = 2
if task8_slope == task9_slope:
    print("The slopes are equal.")
elif task8_slope > task9_slope:
    print("The slope from task 8 is steeper than the slope from task 9.")
else:    
    print("The slope from task 9 is steeper than the slope from task 8.")

#Exercise 11
x=-3
y = x**2 + 6*x + 9
print(f"The value of y when x is -3 is: {y}")

#Exercise 12
falsy_statment = len("python") != len("dragon")
print(f"The falsy statement is: {falsy_statment}")

#Exercise 13
if ("on" in "python") and ("on" in "dragon"):
    print("The substring 'on' is found in both 'python' and 'dragon'."  )
else:
    print("The substring 'on' is not found in both 'python' and 'dragon'.")

#Exercise 14
sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("The word 'jargon' is found in the sentence.")
else:
    print("The word 'jargon' is not found in the sentence.")

#Exercise 15
check_on = "on" in "python" and "on" in "dragon"
print(f"The substring 'on' is found in both 'python' and 'dragon': {check_on}")

#Exercise 16
length_of_python = len("python")
length_of_python_float = float(length_of_python)
length_of_python_str = str(length_of_python)

#Exercise 17
num=10
if(num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

#Exercise 18
is_equal= ((7 // 3) == int(2.7) )
print(is_equal)

#Exercise 19
print(type("10") == type(10))

#Exercise 20
print(int(float("9.8")) == 10)

#Exercise 21
hours=int(input("Enter hours: "))
rate=float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is: {pay}")

#Exercise 22
years = int(input("Enter number of years you have lived: "))
seconds_year = 365 * 24 * 60 * 60
age_seconds = years * seconds_year
print(f"You have lived for {age_seconds} seconds.")

#Exercise 23
for i in range (1, 6):
    print(i, i**0, i, i**2, i**3)