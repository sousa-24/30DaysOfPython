#Exercise 1
first,second,third,forth = "Thirty", "Days", "Of", "Python"
print(first,second,third,forth)

#Exercise 2
print("Codigo "+"For "+"All")

#Exercise 3
company = "Coding For All"

#Exercise 4
print(company)

#Exercise 5
print(len(company))

#Exercise 6
print(company.upper())

#Exercise 7
print(company.lower())

#Exercise 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Exercise 9
first_word = company[0:company.index(" ")]
print(first_word)

#Exercise 10
print("Coding" in company)

#Exercise 11
company = company.replace("Coding","Python")
print(company)

#Exercise 12
print(company.replace("All","Everyone"))

#Exercise 13
print(company.split())

#Exercise 14
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))

#Exercise 15
print(company[0])

#Exercise 16
print(company[-1])

#Exercise 17
print(company[10])

#Exercise 18
string1= "Python For Everyone"
acro1= "".join(word[0] for word in string1.split())
print(acro1)

#Exercise 19
string2 = "Coding For All"
acro2 = "".join(word[0] for word in string2.split())
print(acro2)

#Exercise 20
print("Coding For All".index("C"))

#Exercise 21
print("Coding For All".index("F"))

#Exercise 22
print("Coding For All".rfind("l"))

#Exercise 23/26
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))


#Exercise 24
print(sentence.rfind("because"))

#Exercise 25/27
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:(sentence.rfind("because"))+len("because")])

#Exercise 28
sentence = "Coding For All"
print(sentence.startswith("Coding"))

#Exercise 29
print(sentence.endswith("Coding"))

#Exercise 30
sentence = "   Coding For All      "
print(sentence.strip())

#Exercise 31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#Exercise 32
libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" # ".join(libs))

#Exercise 33
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

#Exercise 34
print("Name\tAge\tCountry\t\tCity\nDiogo\t28\tPortugal\tPorto")

#Exercise 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of the circle with {radius} is {area} meters square.")

#Exercise 36
num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} % {num2} = {num1%num2}")
print(f"{num1} // {num2} = {num1//num2}")
print(f"{num1} ** {num2} = {num1**num2}")
