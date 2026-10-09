# Data-Structure-and-Algorithm-Assignment-1
Expression Evaluator using Custom Stack Data Structure

A Python program that parses and evaluates mathematical expressions read from an input file (input.txt) using a custom stack data structure implementation. The evaluated results are formatted and written to an output file (output.txt) with separator dashes matching the required submission style.

Features

Custom Stack Implementation: Implements push, pop, peek, is_empty, and size methods without relying on external stack libraries.

Infix Expression Parsing: Processes mathematical expressions respecting standard operator precedence rules and parenthetical grouping.

Supported Operators:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Parentheses ((, ))

Formatted Output File: Formats results clean as whole numbers or decimals followed by dashed line separators (-----).

File Structure

.
├── expression_evaluator.py   # Main Python source code
├── input.txt                  # Input file containing math expressions
├── output.txt                 # File generated after running the program
└── README.md                  # Instructions and documentation



Input & Output File Format

Input Format (input.txt)

Each line in input.txt should contain a single valid mathematical expression. Expressions may contain whitespace between tokens.

Example input.txt:

(10 + 3) * 1
5 + (3 * 4)
20 / 2 + 10
(8 + 2) * (5 - 3)



Output Format (output.txt)

The output file replaces each expression with its computed numerical result and includes a dashed separator line (-----) directly underneath each answer.

Example generated output.txt:

13
-----
17
-----
20
-----
20
-----



How to Run the Program

Prerequisites

Python 3.6 or higher installed on your system.

Execution Steps

Prepare the Input File:
Ensure input.txt exists in the same directory as the Python script and contains the math expressions you wish to evaluate.

Run the Script:
Open a terminal or command prompt in the project directory and execute:

python expression_evaluator.py



(Note: On systems where both Python 2 and Python 3 are installed, use python3 expression_evaluator.py)

Check Results:
Open output.txt to view the calculated output.

Assumptions and Limitations

Operator Precedence:

Precedence follows standard arithmetic rules: Multiplication (*) and Division (/) take higher precedence over Addition (+) and Subtraction (-).

Expressions inside parentheses (...) are evaluated first.

Number Formats:

Multi-digit numbers and floating-point numbers (decimals) are supported.

If an expression evaluates to a whole integer (e.g., 13.0), it is formatted and printed as an integer (13).

Unary Operators:

Explicit negative numbers (e.g., -5 + 3 or 3 * -2) are not explicitly handled as unary minus. All operands should be non-negative or enclosed appropriately (e.g., (0 - 5) + 3).

Error Handling & Malformed Input:

In case of division by zero or malformed syntax that cannot be recovered, an Error message is written to output.txt for that specific entry, followed by the separator line (-----).
