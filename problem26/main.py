"""Permutations of a List

Input: [1, 2, 3]

Output: [[1,2,3], [1,3,2], ..., [3,2,1]]"""
from itertools import count


def permute(nums):
    result = []
    def backtrack(path, used):
        print(f"Path: {path}, Used: {used}")
        if len(path) == len(nums):
            result.append(path)
            return

        for i in range(len(nums)):
            if nums[i] in used:
                continue
            backtrack(path + [nums[i]], used + [nums[i]])
    backtrack([], [])
    print(result)

#permute([1,2,3])

"""Problem: Generate all valid parentheses
Input:
An integer n representing pairs of parentheses.

Output:
Return all combinations of well-formed parentheses with n pairs.

Example:

Input: n = 3

Output:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

def combo_pairs(n):
    result = []
    def backtrack(path, open, close):
        if len(path) == 2 * n:
            result.append(path)
            return
        if open < n:
            backtrack(path+'(', open+1, close)
        if close < open:
            backtrack(path+')', open, close+1)
    backtrack('', 0, 0)
    print(result)

combo_pairs(4)
