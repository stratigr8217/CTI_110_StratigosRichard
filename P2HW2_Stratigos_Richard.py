#Richard Stratigos
#10/08/2024
#P2HW1
#Enter and calulate grading averages

#Get Module grades

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
print()

#Calculate and display results

student_grades = [module1, module2, module3, module4, module5, module6]

print("------------Results------------")
if student_grades: 
    lowest_grade = min(student_grades)
    highest_grade = max(student_grades)
    sum_of_grades = sum(student_grades)
    average_grade = sum_of_grades / len(student_grades)

#Display the results
      
print(f"Lowest Grade: {lowest_grade:.2f}")
print(f"Highest Grade: {highest_grade:.2f}")
print(f"Sum of Grades: {sum_of_grades:.2f}")
print(f"Average Grade: {average_grade:.2f}")
print("------------------------------------------")
