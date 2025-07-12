"""
8. Combination Sum
Input: candidates = [2,3,6,7], target = 7
Output:

[[2,2,3],[7]]
➡️ Pick numbers that sum to the target, using each number unlimited times (or only once in variations).

✅ Example 1:
candidates = [2, 3, 5]
target = 8
Valid combinations:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
📌 Note: You can reuse the same number unlimited times.

"""

class Combination:
    def __init__(self, candidates, target):
        self.candidates = candidates
        self.target = target
        self.result = []

    def permute(self):
        def backtrack(start, path, total):
            if total == self.target:
                self.result.append(path)
            if total > self.target:
                return
            for i in range(start, len(self.candidates)):
                backtrack(i, path+[self.candidates[i]], total + self.candidates[i])
        backtrack(0, [], 0)
        print(self.result)


data = [2, 3, 6, 7]
t = 7
Combination(data, t).permute()

"""
2. Combination Sum II (Leetcode 40)
Each number can be used only once.

The input can contain duplicates, but combinations must be unique.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
👉 You need to sort first and skip duplicates."""

class Combo:
    def __init__(self, candidates, target):
        self.candidates = sorted(candidates)
        self.target = target
        self.result = []

    def combination(self):
        def backtrack(start, path, total):
            if total > self.target:
                return
            if total == self.target:
                self.result.append(path)
            for i in range(start, len(self.candidates)):
                if i > start and self.candidates[i] == self.candidates[i - 1]:
                    continue
                backtrack(i+1, path+[self.candidates[i]], total+self.candidates[i])
        backtrack(0, [], 0)
        print(self.result)

cand = [10,1,2,7,6,1,5]
tar = 8
combo = Combo(cand,tar)
combo.combination()


