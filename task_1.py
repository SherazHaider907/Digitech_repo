def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'


def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 & 100")
        except:
            print("Invalid input. Please enter a number.")


# Main Program
name = input("Enter student name: ")

# validate number of subjects
while True:
    try:
        num_subjects = int(input("How many subjects? "))
        if num_subjects > 0:
            break
        else:
            print("Enter a number greater than 0")
    except:
        print("Please enter a valid number!")


subjects = []
marks = []

for i in range(num_subjects):
    print(f"\nSubject {i+1}")

    # validate subject name
    while True:
        subject = input("Enter subject name: ")
        if subject.strip() != "":
            break
        else:
            print("Subject name cannot be empty!")

    subjects.append(subject)

    mark = get_valid_marks(subject)
    marks.append(mark)


total = sum(marks)
percentage = total / num_subjects
grade = calculate_grade(percentage)


# Output
print("\nSTUDENT REPORT")
print("Name:", name)

print("\nSubjects & Marks:")
for subject, mark in zip(subjects, marks):
    print(subject, ":", mark)

print("\nTotal:", total, "/", num_subjects * 100)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)