# PROBLEM 1
# Create a variable that holds the value of your first name.
name = "Tyson"

# PROBLEM 2
# Create a variable that holds the value of your favorite number.
my_number = 21

# PROBLEM 3
# Create a variable that holds a boolean value representing if your hair is brown.
my_hair = False

# PROBLEM 4
# Print your first name, by printing the variable created in problem 1.
print(name)

# PROBLEM 5
#  Create a variable called `loves_code` and set it equal to true.
#  Check to see if `loves_code` is equal to true or false.
#  If it is true, print "I love to code!"
#  If it is not, print "Coding has it's challenges."
loves_code = True

if loves_code == True:
    print("I love to code!")
else:
    print("Coding has it's challenges")

# PROBLEM 6
# Create an array called `colors` and set it equal to a list of at least five colors.
colors = ["Dodger Blue", "Neon Pink", "Sunset Orange", "Steel Grey", "Aztec Gold"]

# Problem 7
# Using bracket syntax, print out the last item in your colors array.
color = colors[len(colors) - 1]
print(color)

# For problems 8-9, use the following line of code:
numbers = [1,2,3,4,5,6,7,8,9,10]

# Problem 8
# Use a for-in loop to iterate over the `numbers` array and print each number.
for new_number in numbers:
    print(new_number)

# Problem 9
# Create an empty array called `even_numbers`.
# Use a for-in loop to iterate over the `numbers` array, and if a number is even, add  it to the `even_numbers` array.
even_numbers = []

for even_numbers in range(4, 15, 2):
    print(even_numbers)


# Problem 10
# Do not edit the code below.
score = 74
# Do not edit the code above.

# Determine if the letter grade of the given variable 'score'. If the variable is a 90 or above, console-log an 'A', between 80 and 89, console-log a 'B', between 70 and 79, 'C', between 60 and 69, 'D', and anything below 60 should console-log an 'F'.
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score <= 59:
    print("F")

# Problem 11
# Create a variable called 'changeMyMind' and set it equal to true.
# Check to see if changeMyMind is set to true or false, if it is true, change the status to false, if it is false, change the status to true.
changeMyMind = True
if changeMyMind == True:
    changeMyMind = False
else:
    changeMyMind = True

# ADVANCED

# For problems 12-15, use the following line of code:
friends = ['Joe', 'Sally', 'Camilo', 'Perry', 'Susan']

# Problem 12
# Research to find the Python method that allows you to add an element to the end of the array (similar to push() in JavaScript), then add a name to the end of the `friends` array.
friends.append('Ariel')

# Problem 13
# Print out the total amount of elements in the `friends` array. The Python method you are looking for is similar to the JavaScript property `.length`.
print(len(friends))

# Problem 14
# Add a name into the third position in the array (index 2). Make sure you are not overwriting the value that is already there.
friends.insert(2,'Jimmy')

# Problem 15
# Remove the last item in the array (try to think about how you can do this dynamically, meaning, if the array contents were to change, your code would still work).
friends.pop(4)