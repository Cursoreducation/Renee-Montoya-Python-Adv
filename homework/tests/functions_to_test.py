class Calculator:
    """ A simple calculator App"""

    def add(self, x, y):
        """Add Function"""
        return x + y

    def subtract(self, x, y):
        """Subtract Function"""
        return x - y

    def multiply(self, x, y):
        """Multiply Function"""
        return x * y

    def divide(self, x, y):
        """Divide Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')

        return x / y
