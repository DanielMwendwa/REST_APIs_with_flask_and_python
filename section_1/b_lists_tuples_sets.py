my_variable = "hello"

grade_one = 77
grade_two = 80 
grade_three = 90
grade_four = 95
grade_five = 100

print((grade_one + grade_two + grade_three + grade_four + grade_five) / 3)

# Lists
grades = [77, 80, 90, 95, 100, 105, 107] # ordered
print(sum(grades) / len(grades))

# Tuples
tuple_grades = (77, 80, 90, 95, 100, 105, 107, 108, 109) #immutable
print(tuple_grades)
tuple_grades += (100,)
print(tuple_grades)

# Sets
set_grades = {77, 80, 90, 100, 100} # unique & unordered
set_grades.add(60)
print(set_grades)

# Set operations
set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

# Difference 
print({1, 2, 3, 4}.difference({1, 2}))

# Intersection - opposite of difference
print(set_one.intersection(set_two))

# Union - addition
print(set_one.union(set_two))


