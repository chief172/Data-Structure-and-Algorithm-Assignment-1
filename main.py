class Stack:
    """1. Create a Stack class to handle stack operators (push, pop, peek)"""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def precedence(op):
    """Helper to define precedence for operators (+, -, *, /)"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def apply_op(a, b, op):
    """Executes basic arithmetic operations"""
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b != 0 else 0
    return 0


def evaluate_expression(expression):
    """
    2. Parses and evaluates mathematical expressions using a stack.
    Handles operators (+, -, *, /), parentheses, and precedence rules.
    """
    values = Stack()
    ops = Stack()
    i = 0

    def process_top_op():
        if ops.is_empty() or values.size() < 2:
            return
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.push(apply_op(val1, val2, op))

    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        if char == '(':
            ops.push(char)

        elif char.isdigit() or char == '.':
            val_str = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                val_str += expression[i]
                i += 1
            val = float(val_str) if '.' in val_str else int(val_str)
            values.push(val)
            i -= 1

        elif char == ')':
            while not ops.is_empty() and ops.peek() != '(':
                process_top_op()
            if not ops.is_empty() and ops.peek() == '(':
                ops.pop()

        elif char in ('+', '-', '*', '/'):
            while (not ops.is_empty() and ops.peek() != '(' and
                   precedence(ops.peek()) >= precedence(char)):
                process_top_op()
            ops.push(char)

        i += 1

    while not ops.is_empty():
        if ops.peek() == '(':
            ops.pop()
        else:
            process_top_op()

    return values.pop() if not values.is_empty() else 0


def process_file(input_filename="input.txt", output_filename="output.txt"):
    """
    3. Reads expressions from input.txt, evaluates each expression.
    4. Writes results to output.txt with dashed line separators below each result.
    """
    try:
        with open(input_filename, "r") as infile:
            lines = infile.readlines()

        evaluated_results = []

        for line in lines:
            line_stripped = line.strip()

            # Skip empty dashed lines if input.txt contains dashed lines from previous output
            if not line_stripped or line_stripped.startswith("-"):
                continue

            try:
                result = evaluate_expression(line_stripped)
                # Format to integer if whole number (e.g., 13 instead of 13.0)
                formatted_result = int(result) if isinstance(result, float) and result.is_integer() else result
                
                # Append result followed by dashed line separator
                evaluated_results.append(f"{formatted_result}\n")
                evaluated_results.append("-----\n")
            except Exception as e:
                evaluated_results.append(f"Error\n-----\n")

        with open(output_filename, "w") as outfile:
            outfile.writelines(evaluated_results)

        print(f"Successfully evaluated expressions. Output written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'. Make sure the file exists.")


if __name__ == "__main__":
    process_file()