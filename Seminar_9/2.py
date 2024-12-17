class StackCalculator:
    def __init__(self):
        self.stack = []

    def evaluate(self, expression):
        operators = {'+': lambda a, b: a + b,
                     '-': lambda a, b: a - b,
                     '*': lambda a, b: a * b,
                     '/': lambda a, b: a / b if b != 0 else None}

        for token in expression.split():
            if token.isdigit():
                self.stack.append(int(token))
            elif token in operators:
                if len(self.stack) < 2:
                    return "Некорректное выражение"
                b = self.stack.pop()
                a = self.stack.pop()
                result = operators[token](a, b)
                if result is None:
                    return "Деление на ноль"
                self.stack.append(result)
            else:
                return "Некорректное выражение"

        if len(self.stack) != 1:
            return "Некорректное выражение"

        return self.stack.pop()


stack_calculator = StackCalculator()
expression = input()  
result = stack_calculator.evaluate(expression)
print(result)

# Пример Ввод: 2 3 - 12 10 - * 4 2 / +     это тоже самое что и (2-3)*(12-10)+4/2 = 0          Вывод: 0
