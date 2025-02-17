# Calculate student's final grade
name = input("Enter student's name: ")

# The system asks for the student's grades
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))

# Calculate the final grade 20%
final_grade = (grade1 + grade2 + grade3) / 3

# Display student's name in uppercase
uppercase_name = name.upper()
# Display student's name in lowercase
lowercase_name = name.lower()

# Print the results
print("Grade 1: ", grade1)
print("Grade 2: ", grade2)
print("Grade 3: ", grade3)
print("Final grade: ", final_grade)
print("Name in Uppercase: ", uppercase_name)
print("Name in Lowercase: ", lowercase_name)

# Conditions to display the grade
if final_grade < 5:
    print("Grade: FAIL")
elif final_grade >= 5 and final_grade < 7:
    print("Grade: PASS")
elif final_grade >= 7 and final_grade < 9:
    print("Grade: GOOD")
else:
    print("Grade: EXCELLENT")


def calculate_final_grade(grade1, grade2, grade3):
    """Calculates the average of three grades."""
    return (grade1 + grade2 + grade3) / 3

def determine_letter_grade(final_grade):
    """Determines the letter grade based on the final numerical grade."""
    if final_grade >= 90:
        return "A"
    elif final_grade >= 80:
        return "B"
    elif final_grade >= 70:
        return "C"
    elif final_grade >= 60:
        return "D"
    else:
        return "F"

num_students = 5

for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    grade1 = float(input(f"Enter grade 1 for {name}: "))
    grade2 = float(input(f"Enter grade 2 for {name}: "))
    grade3 = float(input(f"Enter grade 3 for {name}: "))

    final_grade = calculate_final_grade(grade1, grade2, grade3)
    letter_grade = determine_letter_grade(final_grade)

    print(f"\n--- Student {i+1} ---")
    print(f"Name: {name.upper()}")
    print(f"Final Grade: {final_grade:.2f}")  # Format to 2 decimal places
    print(f"Letter Grade: {letter_grade}")