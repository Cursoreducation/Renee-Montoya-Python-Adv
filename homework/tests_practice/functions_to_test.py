class Calculator:
    """ A simple calculator App"""

    @staticmethod
    def add(x, y):
        """Add Function"""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Subtract Function"""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiply Function"""
        return x * y

    @staticmethod
    def divide(x, y):
        """Divide Function"""
        try:
            if y == 0:
                raise ValueError("It can't to divide by zero!")
            else:
                return x / y
        except ValueError:
            print("It can't to divide by zero!")
