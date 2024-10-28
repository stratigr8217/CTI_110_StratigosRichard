# Richard Statigos
# 10/28/2024
# For-Loop Examples

# For-Loop with range - one parameter

for item in range(5):
    print(item)

print()

# For-Loop with range - two parameters
# Range (start,stop) - stop is not inclusive

for apple in range(3, 10):
    print(apple)

# For-Loop with range - three parameters
# Range function (start,stop,step) - stop is not inclusive

for dog in range(2,21,2:):
    print(dog)

# Print pairs of 5's

print("PAIRS OF CATS BY 5")
for cat in range(5,21,5:):
    print(cat)

# Print all values in a list

trees = ["Pine", "Dogwood", "Palm", "Oak"]

print("Lemme tell ya about trees!")

for tree in trees:
    print(tree, "Tree")
    print("************")

num_list = [0, -7, 2, 8]
num_sum = 0
for num in num_list:
    print(num + 5)
    num_sum += num
