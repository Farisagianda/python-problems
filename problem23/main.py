"""
Problem:
Write a function flatten(lst) that takes a nested list lst (which may contain integers or further nested lists of integers) and returns a flat list of all integers in the same order they appear.

Example:
flatten([1, [2, [3, 4], 5], 6])
# Output: [1, 2, 3, 4, 5, 6]

Constraints:

Do not use any built-in functions like itertools.chain or sum(..., []).

Use recursion.

After implementing, discuss the time and space complexity of your solution.

"""

## recursive

def flatten(lis):
    res = []

    def subset(subset_lis):
        for l in subset_lis:
            if isinstance(l, list):
                subset(l)
            else:
                res.append(l)
    subset(lis)
    print(res)
    return res

## iterative

def flatten_list(nested):
    result = []

    def recurse(stack):
        while stack:
            item = stack.pop()
            if isinstance(item, list):
                # Push back the list contents in reverse order so pop() gets left to right
                stack.extend(reversed(item))
            else:
                result.append(item)

    # Make a copy of the input and reverse it so we process left-to-right
    recurse(nested[::-1])
    return result

if __name__ == "__main__":
    n = [1, [2, [3, 4], 5], 6]
    print(flatten_list(n))  # Output: [1, 2, 3, 4, 5, 6]
