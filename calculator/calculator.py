#Calculator Script
from art import logo


#Define Class of MathOperations to perform arithmetic operations
class MathOperations():
	def __init__(self):
		self.operand_dict = {
  						"+" : self.add,
						"-" : self.subtract,
						"*" : self.multiply,
						"/" : self.divide,
							 }
		
	def add(self, num1, num2):
		total = num1 + num2
		return total

	def subtract(self, num1, num2):
		total = num1 - num2
		return total

	def multiply(self, num1, num2):
		total = num1 * num2
		return total

	def divide(self, num1, num2):
		if num2 == 0:
			return "Error: Attempting to divide by 0"
		total = num1 / num2
		return total

#main function
def main():
	print(logo)
	print("Welcome to the Calculator Script")
	result = None
	while True:
		num1, operation_type, num2 = get_input(result)
		math_ops = MathOperations()
		if operation_type in math_ops.operand_dict:
			result = math_ops.operand_dict[operation_type](num1,num2)
			print(f"{num1} {operation_type} {num2} = {result}")
		else:
			print(f"Invalid operation type for: {operation_type}")
			
		choice = input(f"Type 'y' you continue calculating with {result}, type 'n' to start a new calculation, or type 'q' to quit the program: ").lower()
		if choice == "y":
			continue
		elif choice == "n":
			result = None
		elif choice == "q":
			break
		else:
			print(f"Error: {choice} is not valid, please enter: 'y' or 'n': ")
				
#Gets user's input: n1, operand type, n2
def get_input(previous_result=None):
	try: 
		if previous_result is not None:
			number_1 = previous_result
		else:
			number_1 = float(input("Please provide me with the first number: "))
			
		print("+\n-\n*\n/\n")
		operation_type = input("Pick an operation: ")
		number_2 = float(input("Please provide me with the second number: "))
	except Exception as e:
		print("Error: ", str(e))
		return get_input()

	return (number_1, operation_type, number_2)

if __name__ == "__main__":
	main()
		