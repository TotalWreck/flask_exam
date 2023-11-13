class SimpleCalculator:
    def __init__(self):
        self.result = None

    def add(self, a, b):
        self.result = a + b

    def subtract(self, a, b):
        self.result = a - b

simple_calculator = SimpleCalculator()