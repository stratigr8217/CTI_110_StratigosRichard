# Richard Stratigos
# 10/30/2024
# P4HW1
# Build on P2HW1 to include a loop, dropping lowest score, and adding printed letter grades

# Ask the user how many scores they would like to enter
num_scores = input("How many scores would you like to enter? ")

# Ensure the input is a valid positive integer
while not num_scores.isdigit() or int(num_scores) <= 0:
    print("INVALID Score entered!!!!!")
    print("Score shpould be between 0 and 100")
    num_scores = input("How many scores would you like to enter? ")

num_scores = int(num_scores)

# Initialize an empty list to store valid scores

student_grades = []

# Loop to collect the specified number of scores

for i in range(1, num_scores + 1):
    score = input(f"Enter grade for Module {i}: ")

# Validate if the score is a number and between 0 and 100
    
    while not (score.replace('.', '', 1).isdigit() and 0 <= float(score) <= 100):
        print("INVALID Score entered!!!!!")
        print("Score should be between 0 and 100")
        score = input(f"Enter grade for Module {i} again: ")

# Add valid score to the list

    student_grades.append(float(score))

# Calculate and display results

if student_grades:
    lowest_grade = min(student_grades)
    student_grades.remove(lowest_grade)  # DROP THE LOWEST SCORE
    
# Calculate the sum and average of the remaining grades

    sum_of_grades = sum(student_grades)
    average_grade = sum_of_grades / len(student_grades)

# Determine the letter grade based on the average

    if average_grade >= 90:
        letter_grade = 'A'
    elif average_grade >= 80:
        letter_grade = 'B'
    elif average_grade >= 70:
        letter_grade = 'C'
    elif average_grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

# Display the results

    print("------------Results------------")
    print(f"Lowest Score: {lowest_grade:.2f}")
    print(f"Modified List: {student_grades}")
    print(f"Scores Average: {average_grade:.2f}")
    print(f"Grade: {letter_grade}")
    print("------------------------------------------")
else:
    print("Exiting program...")
