a = 5
b = 20
my_variable = 56
any_variable_name = 10 

string_variable = "hello"
single_quotes = 'strings can have single quotes'

print(my_variable)
print(string_variable) 

##

def my_print_method(my_argument):
	print(my_argument)

my_print_method("hello, world!")

def my_multiple_method(number_one, number_two):
	return number_one * number_two

result = my_multiple_method(5, 3)
print(result)


my_print_method(my_multiple_method(5,3))

