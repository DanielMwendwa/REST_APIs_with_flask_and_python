lottery_player_dict = {
	'name': 'Rolf',
	'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
	def __init__(self, name):
		self.name = name
		self.numbers = (5, 9, 12, 3, 1, 21)

	def total(self):
		return sum(self.numbers)

# player_one = LotteryPlayer("Rolf")
# player_two = LotteryPlayer("John")
# player_one.numbers = (1, 2, 3, 6, 7, 8)

# print(player_one.name)
# print(player_one.numbers)
# print(player_one.total())

# print(player_one == player_two) # distinct
# print(player_one.name == player_two.name) 
# print(player_one.numbers == player_two.numbers)


class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	# @classmethod
	# def go_to_school(cls):
	# 	print("I'm going to school.")
	# 	print("I'm a {}".format(cls))

	@staticmethod
	def go_to_school():
		print("I'm going to school.")

anna = Student("Anna", "MIT")
anna = Student("Rolf", "Oxford")

anna.marks.append(56)
print(anna.marks)
print(anna.average())
anna.go_to_school()
Student.go_to_school()