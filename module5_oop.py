import sys

class NumberSearcher:
    def __init__(self):
        self.nums = []

    def populate_from_input(self):
        try:
            user_input = input("Input a positive integer: ")
            n = int(user_input)
        except ValueError:
            print("Invalid input.")
        
        self.nums = []
        print("Input the integers:")
        
        for i in range(n):
            try:
                read_num = input(f"Input integer {i+1}: ")
                self.nums.append(int(read_num))
            except ValueError:
                print("Invalid input.")
    
    # returns the index (base 1) of x in the list, or -1 otherwise
    def search(self, x):
        for i in range(len(self.nums)):
            if self.nums[i] == x:
                return i + 1
        return -1

    def populate_and_search(self):
        x = input("Input a number to search for: ")
        try:
            result = self.search(int(x))
            print(result)
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    number_searcher = NumberSearcher()
    number_searcher.populate_from_input()
    number_searcher.populate_and_search()
