"""
Input: "{[()]}"
Output: True

Input: "{[(])}"
Output: False

Task: Write a function `is_balanced(s: str) -> bool` that uses a stack to validate parentheses.

"""

def main(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs and stack:
            if stack[-1] == pairs[i]:
                stack.pop()
            else:
                print(False)
                return False
        else:
            print(False)
            return False
    print(not stack)
    return not stack





if __name__ == "__main__":
    s = "{[()]}"
    #s = "{[))]}"
    #s = "{[]}"
    s = "{[()]}"
    #s = "{[()()]}"
    s = "}}}}}"
    main(s)