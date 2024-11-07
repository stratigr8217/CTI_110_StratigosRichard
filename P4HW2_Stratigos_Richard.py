# Richard Stratigos
# 11/07/2024
# P4HW2
# Build on P3HW2 to add multiple employees and totals for all variables


# Initialize totals

total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Start of employee loop

employee_name = input("Enter the employee's name (or 'Done' to terminate): ")

while employee_name.lower() != "done":
    
# Get employee details

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

# Calculate overtime and regular pay

    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked
    regular_pay = regular_hours * pay_rate

# Calculate overtime if applicable

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40  # regular hours are capped at 40
        regular_pay = regular_hours * pay_rate

# Overtime pay is 1.5 times the regular pay rate

    overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate total gross pay

    gross_pay = regular_pay + overtime_pay

# Update totals

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

# Display individual results

    print("----------------------------------")
    print(f"Employee name:  {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
    print("------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.2f}${pay_rate:<12.2f}{overtime_hours:<12.2f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<12.2f}")
    print()

# Ask for the next employee or 'Done' to terminate

    employee_name = input("Enter employee's name or 'Done' to terminate: ")

# After the loop ends, display totals

print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
