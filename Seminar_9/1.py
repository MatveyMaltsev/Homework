class ExpressionConverter:
    def __init__(self):
        self.operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    def infix_to_postfix(self, expression):
        operator_stack = []
        output = []

        for char in expression:
            if char.isdigit():
                output.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while (operator_stack and
                       self.operator_priority[operator_stack[-1]] >= self.operator_priority[char]):
                    output.append(operator_stack.pop())
                operator_stack.append(char)

        while operator_stack:
            output.append(operator_stack.pop())

        return ''.join(output)

    def infix_to_prefix(self, expression):
        reversed_expression = expression[::-1]
        reversed_expression = (reversed_expression
                                .replace('(', '#')
                                .replace(')', '(')
                                .replace('#', ')'))

        reversed_postfix = self.infix_to_postfix(reversed_expression)
        prefix = reversed_postfix[::-1]

        return prefix


expression_converter = ExpressionConverter()
expression = input().replace(" ", "")  # Удаляем пробелы из выражения

postfix_notation = expression_converter.infix_to_postfix(expression)
prefix_notation = expression_converter.infix_to_prefix(expression)

print(postfix_notation)
print(prefix_notation)
