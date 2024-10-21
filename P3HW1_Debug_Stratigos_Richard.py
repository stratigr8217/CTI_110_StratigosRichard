#Richard Stratigos
#10/18/2024
#P3HW1_Debug
#Identify and correct syntax errors to make the program run


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
              
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results

print()
print('----------Results----------')
print(f"{'Lowest grade:':<18}{low:<25}")
print(f"{'Highest grade:':<18}{high:<25}")
print(f"{'Sum of grades:':<18}{total:<25}")
print(f"{'Average:':<18}{avg:<25}")

# Determine letter grade for average

print('---------------------------')
if avg >= 90:
    print('Your grade is: A')
elif avg > 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')






