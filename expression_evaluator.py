# Expression Evaluator using Python
# This program evaluates a mathematical expression entered
# by the user. It supports addition, subtraction, multiplication,
# division and parentheses while following operator precedence.
import math
# Evaluate Expression Function
def evaluate_expression(expr):

    try:
        result = eval(expr)
        return result

    except Exception:
        return "Invalid Expression"
# Display Report
def display_result(expression, result):

    print("EXPRESSION REPORT")

    print("Input Expression :", expression)

    print("Result           :", result)

    print("=======================================\n")
def main():

    print("EXPRESSION EVALUATOR")

    expression = input("\nEnter a mathematical expression: ")

    result = evaluate_expression(expression)

    display_result(expression, result)


if __name__ == "__main__":
    main()