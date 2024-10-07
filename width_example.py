#Richard Stratigos
#10/07/2024
#Width example
#Formating output using the f-string

#Variables

name = "Bane"
address = "League of Shadows HQ, Location Unknown"
bribe = 10000.69520
kill_count = 83
contract = 25000.69420
isDeadly = True

#Print the characters X amount of times

print("*-" *25)

print(f"{'Name:':<18}{name:<25}")

print(f"{'Address:':<18}{address:<25}")

print(f"{'Bribe for your life:':<18}${bribe:<25,.2f}")

print(f"{'Humans Neutralized.. so far:':<18}{kill_count:<25}")

print(f"{'Contract Minumum:':<18}${contract:<25,.2f}")

print(f"{'Is Bane Deadly?:':<18}{str(isDeadly):<25}")
