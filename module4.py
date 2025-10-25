import sys

def read_numbers_from_input():
	try:
		user_input = input("Input a positive integer: ")
		n = int(user_input)
	except ValueError:
		print("Invalid input.")
		exit()

	nums = []
	for i in range(n):
		try:
			read_num = input("Input an integer: ")
			nums.append(int(read_num))
		except ValueError:
			print("Invalid input.")
	return nums

def search_number(nums, x):
	for i in range(len(nums)):
		if nums[i] == x:
			return i
	return -1

if __name__ == "__main__":
	nums = read_numbers_from_input()
	x = input("Input a number to search for: ")
	try:
		result = search_number(nums, int(x))
		if result != -1:
			print(f"Number found at index: {result + 1}")
		else:
			print("Number not found.")
	except ValueError:
		print("Invalid input.")