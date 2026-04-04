"""A simple expression calculator with logic bugs."""

import operator


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

# Bug 1: precedence is wrong — * and / should be higher than + and -
PRECEDENCE = {
    "+": 2,
    "-": 2,
    "*": 1,
    "/": 1,
    "^": 3,
}


def tokenize(expression):
    tokens = []
    current_num = ""
    for char in expression:
        if char.isdigit() or char == ".":
            current_num += char
        elif char in OPERATORS or char in "()":
            if current_num:
                tokens.append(float(current_num))
                current_num = ""
            tokens.append(char)
        elif char == " ":
            if current_num:
                tokens.append(float(current_num))
                current_num = ""
    if current_num:
        tokens.append(float(current_num))
    return tokens


def to_postfix(tokens):
    output = []
    op_stack = []

    for token in tokens:
        if isinstance(token, float):
            output.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            if op_stack:
                op_stack.pop()
        elif token in OPERATORS:
            while (op_stack and op_stack[-1] != "(" and
                   op_stack[-1] in PRECEDENCE and
                   # Bug 2: should be >= for left-associative operators
                   PRECEDENCE[op_stack[-1]] > PRECEDENCE[token]):
                output.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        output.append(op_stack.pop())

    return output


def evaluate_postfix(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in OPERATORS:
            b = stack.pop()
            a = stack.pop()
            stack.append(OPERATORS[token](a, b))
    return stack[0]


def calculate(expression):
    tokens = tokenize(expression)
    postfix = to_postfix(tokens)
    return evaluate_postfix(postfix)


if __name__ == "__main__":
    tests = [
        ("2 + 3", 5.0),
        ("10 - 4", 6.0),
        ("3 * 4", 12.0),
        ("15 / 3", 5.0),
        ("2 + 3 * 4", 14.0),       # Should be 14, not 20
        ("(2 + 3) * 4", 20.0),
        ("10 - 2 - 3", 5.0),       # Should be 5, not 11
        ("2 ^ 3", 8.0),
        ("100 / 10 / 2", 5.0),     # Should be 5, not 20
    ]

    all_passed = True
    for expr, expected in tests:
        result = calculate(expr)
        status = "PASS" if abs(result - expected) < 0.001 else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"{status}: {expr} = {result} (expected {expected})")

    if all_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests FAILED!")
