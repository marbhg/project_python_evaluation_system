# Calculate student's final grade
name = input("Enter student's name: ")

# The system asks for the student's grades
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))

# Calculate the final grade
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
