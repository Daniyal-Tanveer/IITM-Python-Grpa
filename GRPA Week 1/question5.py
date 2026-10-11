'''
Question 
GrPA 5 - (Input Output and Type conversion) - GRADED
Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")
Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.
Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".
Note: Finding the tenth_month will be a bit of challange. If you are stuck open the below hint.
'''

#Answer 

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.

# 1. Read age as an integer
age = int(input()) 

# 2. Read date of birth (dob) as a string
dob = input() 

# 3. Split dob by '/' and convert each part into an integer
day, month, year = map(int, dob.split('/')) 

# 4. Calculate fifth birthday by adding 5 to the birth year
fifth_birthday = f"{day}/{month}/{year + 5}" 

# 5. Calculate last birthday by adding current age to the birth year
last_birthday = f"{day}/{month}/{year + age}" 

# 6. Calculate the date exactly 10 months after birth
new_month = (month + 10 - 1) % 12 + 1
new_year = year + (month + 10 - 1) // 12
tenth_month = f"{day}/{new_month}/{new_year}" 

# 7. Print the three calculated dates separated by a comma and a space
print(tenth_month, fifth_birthday, last_birthday, sep=", ")

# 8. Read weight as a float
weight = float(input()) 

# 9. Separate the integer part (kg) and fractional part (grams)
kg = int(weight)
grams = int(round((weight - kg) * 1000))
weight_readable = f"{kg} kg {grams} grams" 

# 10. Print the human-readable weight string
print(weight_readable)
