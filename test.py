class MathOperations:
    result = 0
    def __init__(self, x):
        self.result = x
    
    def add (self, x, y):
        self.result += x + y
    
    def multiply(self, x, y):
        self.result += x * y
math_ops = MathOperations(20)
math_ops.add (3, 5)
math_ops.multiply(2,4)

print(math_ops.result)