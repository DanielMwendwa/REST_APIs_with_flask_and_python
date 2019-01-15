my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
print(an_equal_list)

multiply_list = [x*3 for x in range(5)]
print(multiply_list)

print(8 % 3) # Remainder

# List of even numbers
print([n for n in range(10) if n % 2 == 0])

people_you_know = ["Rolf", "John", "anna", "GREG"]
normalised_people =  [person.strip().lower() for person in people_you_know]
print(normalised_people)

## Exercise
def who_do_you_know():
	# Ask the user for a list of people they know 
	# Split the string into a list
	# Return that list
	people = input("Enter the names of people you know, separated by comas: ")
	people_list = people.split(",")

	people_without_spaces = [person.strip() for person in people_list]
	
	return people_without_spaces
	