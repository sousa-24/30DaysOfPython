#Exercices: Level 1
#1. Create an empty tuple
tuple_empty =()

#2.
irmas = ("Inês","Mariana")
irmaos = ("Diogo","Carlos")

#3.
familia = irmas + irmaos

#4.
print(len(familia))

#5.
family_members = familia + ("Álvaro","Rosário")
print(family_members)

#Exercices: Level 2
#1.
irmaos = family_members[0:4]
print(irmaos)
pais = family_members[4:]
print(pais)

#2.
fruits = ("banana","orange","mango","lemon")
vegetables = ("tomato","potato","cucumber","onion")
animal_products = ("milk","meat","egg","cheese")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3.
food_stuff_tp=list(food_stuff_tp)
print(type(food_stuff_tp))

#4.
if len(food_stuff_tp) // 2 == 0:
    middle_item = print(food_stuff_tp[len(food_stuff_tp) // 2])
else:    
    middle_item_two = print(food_stuff_tp[len(food_stuff_tp) // 2 - 1])
    middle_item = print(food_stuff_tp[len(food_stuff_tp) // 2])

#5.
first_three = food_stuff_tp[0:3]
print(first_three)
last_three = food_stuff_tp[-3:]
print(last_three)

#6.
del food_stuff_tp

#7.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)