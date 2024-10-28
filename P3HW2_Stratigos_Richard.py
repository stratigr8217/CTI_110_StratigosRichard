# Richard Stratigos
# 10/23/2024
# P3HW2
# Calculate hourly pay and any overtime

# Get employee details

employee_name = input("Enter the employee's name: ")
hours_worked = float(input(f"Enter number of hours worked: "))
pay_rate = float(input(f"Enter employee's pay rate: "))

# Calculate variables

overtime_hours = 0
overtime_pay = 0
regular_hours = hours_worked
regular_pay = regular_hours * pay_rate

# Calculate overtime

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40  # regular hours are capped at 40
    regular_pay = regular_hours * pay_rate
    
# Overtime pay is 1.5 times the regular pay rate

overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate total gross pay

gross_pay = regular_pay + overtime_pay

# Display results

print("----------------------------------")
print(f"Employee name:  {employee_name}")
print()

print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
print("------------------------------------------------------------------------------")
print(f"{hours_worked:<15.2f}${pay_rate:<12.2f}{overtime_hours:<12.2f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<12.2f}")
