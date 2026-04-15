# Taking input
name = input("Enter Name:")

english = float(input("Enter marks for English: "))
math = float(input("Enter marks for Math: "))
science = float(input("Enter marks for Science: "))
computer = float(input("Enter marks for Computer: "))
urdu = float(input("Enter marks for Urdu: "))

# Calculating total

total = english + math + science + computer + urdu

# Calculating percentage

percentage = total / 5

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# result

# Displaying result
print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)