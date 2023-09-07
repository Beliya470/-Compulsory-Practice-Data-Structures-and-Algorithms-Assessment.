def is_balanced(expression):
    stack = []
    bracket_pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    return not stack

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
