"""Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Hint: You might need to store (val, min_so_far) at each level.
"""
class Stacking:
    def __init__(self):
        self.stack = []
        self.min_so_far = []

    def push(self, val):
        if not isinstance(val, int):
            print("Val must be a digit")
            exit(1)
        try:
            self.stack.append(val)
            print(f"{val} pushed to the stack. Stack is now {self.stack}")
            if not self.min_so_far or self.min_so_far[-1] >= val:
                self.min_so_far.append(val)
        except Exception as e:
            print(f"Error in pushing: {e}")

    def pop(self):
        if self.stack:
            print(f"{self.stack[-1]} is being popped from the stack.")
            if self.stack[-1] == self.min_so_far[-1]:
                self.min_so_far.pop()
            self.stack.pop()
            print(f"Stack is now {self.stack}")
        else:
            print("Stack is empty.")

    def top(self):
        if self.stack:
            print(f"Value for top of the stack is: {self.stack[-1]}")
        else:
            print("Stack is empty.")

    def get_min(self):
        if self.min_so_far:
            print(f"Minimum value in stack {self.stack} is: {self.min_so_far[-1]}")
        else:
            print("Stack is empty.")

class Stacking2:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if not isinstance(value, int):
            print("Value is not an integer")
            exit(1)
        if not self.stack or self.stack[-1][-1] >= value:
            min_so_far = value
        else:
            min_so_far = self.stack[-1][-1]
        print(f"{value} is being pushed to the stack.")
        self.stack.append((value, min_so_far))

    def top(self):
        if self.stack:
            print(f"The top value in the stack is {self.stack[-1][0]}")
        else:
            print("Stack is empty")

    def pop(self):
        if self.stack:
            print(f"{self.stack[-1][0]} is being popped from the stack")
            self.stack.pop()
        else:
            print("Stack is empty")

    def get_min(self):
        if self.stack:
            print(f"The min value in the stack is: {self.stack[-1][-1]}.")
        else:
            print("Stack is empty")

if __name__ == "__main__":
    stacked = Stacking2()
    stacked.push(3)
    stacked.push(5)
    stacked.push(2)

    stacked.top()
    stacked.get_min()
    stacked.pop()
    stacked.get_min()