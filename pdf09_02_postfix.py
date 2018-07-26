class Postfix():

    def __init__(self, string):
        self._string = string
        pass

    def evaluate(self):
        operators = '+-*/'
        s = Stack()
        tokens_list = self._expr.split()
        for token in tokens_list:
            if token in operators:
                right = s.pop()
                left = s.pop()
                result = self.eval_math(left, right, token)
                s.push(result)

    def eval_math(self, left, right, op):
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        elif op == "/":
            return left / right
