import re

text = "apple,banana;orange grapes"

# Split by comma or semicolon
result1 = re.split(r"[,;]", text)
print(result1)

# Split by one or more whitespace characters
result2 = re.split(r"\s+", text)
print(result2)

# Split by comma or semicolon, with a maximum of one split
result3 = re.split(r"[,;]", text, maxsplit=1)
print(result3)