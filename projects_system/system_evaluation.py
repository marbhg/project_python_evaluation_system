#Calculate student's final grade
name = input("Enter student's name: ")

# The system asks for the student's grades
def calculate_grade():
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))

# Calculate the final grade 20%
    final_grade = (grade1 + grade2 + grade3) / 3

    # Print the results
    print("Grade 1: ", grade1)
    print("Grade 2: ", grade2)
    print("Grade 3: ", grade3)
    print("Final grade: ", final_grade)
    return final_grade

def student_name(i):
      print(f"\n--- Student {i+1} ---")
      name = input(f"Enter the name of  student {i+1}: ")
      print(f"Name: {name.upper()}")          
    

def determine_letter_grade(final_grade):
    # Conditions to display the grade
    if final_grade < 5:
        print("Grade: FAIL")
    elif final_grade >= 5 and final_grade < 7:
        print("Grade: PASS")
    elif final_grade >= 7 and final_grade < 9:
        print("Grade: GOOD")
    else:
        print("Grade: EXCELLENT")

def calculate_multiples_students():
    num_students = 5

    for i in range(num_students):
        student_name(i)
        final_grade = calculate_grade()  
        print(f"Nota Final: {final_grade:.2f}")
        determine_letter_grade(final_grade)


   