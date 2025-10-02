class Calculator:
    def add(self, a, b):
        return a + b
    
    # add sub operation
    def subtract(self, a, b):
        return a + b
    
    # add mul operation
    def multiply(self, a, b):
        return a * b
    
    # add div operation
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b