# test_stacks.py

from stacks import is_balanced

def test_is_balanced():
    expression1 = "([]{})"
    expression2 = "([)]"
    assert is_balanced(expression1) == True
    assert is_balanced(expression2) == False
