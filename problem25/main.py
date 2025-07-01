"""
🧩 Problem: Generate All Binary Strings of Length n
Goal: Print all possible binary strings of length n.

✅ Example:
For n = 2, output should be:

00
01
10
11
💡 Why this is perfect for beginners:
The choices are simple: at each position, you either place 0 or 1.

No need to track visited states or prune anything.

Easy to visualize recursion and backtracking.
"""

class BinaryGenerator:
    def __init__(self, n):
        self.n = n

    def backtrack(self, current=""):
        if len(current) == self.n:
            print(current)
            return
        self.backtrack(current + "0")
        self.backtrack(current + "1")



if __name__ == "__main__":
    n = 4
    binary_pm = BinaryGenerator(n)
    binary_pm.backtrack()

"""
my_list = [1, 2, 3, 4, 5]
copied_list = my_list

print(copied_list)  # Output: [1, 2, 3, 4, 5]
print(copied_list is my_list) # Output: False (they are different objects)
"""
"""
def backtrack(state):
    if solution_found(state):
        save(state)
        return

    for choice in choices:
        make(choice)
        backtrack(updated_state)
        undo(choice)  # <- This is the key backtracking part!
"""