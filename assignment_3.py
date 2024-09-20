# -*- coding: utf-8 -*-

#CS 175

#Suchit Mudichintala

#restaurant

#set dietary restrictions
vegetarian = False
vegan = False
gluten_free = False

#input questions
response = input(("Is anyone in your party a vegetarian?: ")).lower()
if response == "yes":
  vegetarian = True

response = input(("Is anyone in your party a vegan?: ")).lower()
if response == "yes":
  vegan = True

response = input(("Is anyone in your party a gluten-free?: ")).lower()
if response == "yes":
  gluten_free = True

#new line
print()
print("Here are your restaurant choices: ")

#output restaurant choices
if (not vegetarian) and (not vegan) and (not gluten_free):
  print("Joe's Gourmet Burgers")

if (not vegan) and (not gluten_free):
  print("Mama's Fine Italian")

if (not vegan):
  print("Main Street Pizza Company")

print("Corner Café")
print("The Chef's Kitchen")

#Suchit Mudichintala

#Locker Combination

import random

def lockerCombo():
  myName = "Suchit"

  num1=random.randint(0,39)
  num2=random.randint(0,39)
  num3=random.randint(0,39)

  if (num1==num2 or num2==num3):
    print("\tPlease try again, this is not a valid combination.")
  else:
    print(f"\t{myName}'s locker combination is {num1}-{num2}-{num3}.")
    print("\tThis combination will work.")

lockerCombo()
