# -*- coding: utf-8 -*-
"""final_review (part 2).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_SGfiTLiCb78hhFj_kplSB3M4l072B6c
"""

#Suchit Mudichintala
#CS 175

#Q1. What will the following code return when you call the function?

def multiply_func(a, b = 2):
  return a * b

print(multiply_func(5))
print(multiply_func(5, 3))

# 10
# 15

#Q2. Make a new list containing every second item in the original list x.

x = [1,2,4,5,6,7,8,10]

new_list = x[1::2]
print(new_list)

#Q3. What will the following code return when you run the code?

a = [1,2,3,4,5,6,7,8,9]
d = a[-4:-1]
print(d)

# [6, 7, 8]

#Q4. Write the line of code to access the second sublist and return the last two elements.

nested = [[1,2,3],[4,5,6],[7,8,9]]
print(nested[1][-2:])

#Q5. Write the line of code to reverse each row of the nested list.

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for row in nested_list:
  row.reverse()
print(nested_list)

#Q6. Modify the list of words to output as a hyphenated sentence.

words = ["Deep", "Fried", "wings"]
sentence = "-".join(words)
print(sentence)

#Q7. Write the lines of code to find the last occurrence of a substring within a string and the search is limited to the first 30 characters of the string.

text = "The beach is beautiful, and spending time at beach is always enjoyable!"
substring = "beach"
last_occurrence = text.rfind(substring, 0, 30)
print(last_occurrence)

#Q8. Write the line of code to remove the leading zeros.

number_str = "00012345"
number = int(number_str.lstrip("0"))
print(number)

#Q9. Write the lines of code to display as multiline text.

text = ['Line1 ', 'Line2 ', 'Line3 ']
for line in text:
  print(line)

#Q10. Write a program to calculate the Body Mass Index (BMI) based on user-provided height and weight. If BMI equal or above 25, then the person is overweight. Here is the formula for BMI. Display the result using formatted string.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi >= 25:
  print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
  print(f"Your BMI is {bmi:.2f}. You are not overweight.")