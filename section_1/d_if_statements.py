should_continue = True
if should_continue == True:
	print("Hello")

if should_continue:
	print("Hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

# if person in known_people:
# 	print("You know this person!")

# if person not in known_people:
# 	print("You don't know this peson!")

# if person in known_people:
# 	print("You know this person!")
# else:
# 	print("You don't know this peson!")

if person in known_people:
	print("You know {}!".format(person))
else:
	print("You don't know {}!".format(person))

## Exercise
def who_do_you_know():
	# Ask the user for a list of people they know 
	# Split the string into a list
	# Return that list
	people = input("Enter the names of people you know, separated by comas: ")
	people_list = people.split(",")

	people_without_spaces = []
	for person in people_list:
		people_without_spaces.append(person.strip())
	
	return people_without_spaces

def ask_user():
	# Ask user for a name
	# See if their name is in the list of people they know
	# Print out that they know the person
	person = input("Enter a name of someone you know: ")
	if person in who_do_you_know():
		print("You know {}!".format(person))

ask_user()