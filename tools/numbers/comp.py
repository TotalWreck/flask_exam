class ComplexCalculator:
    def __init__(self):
        self.simp_called = False

    def sum_of_digits(self, number):
        return sum(int(digit) for digit in str(number))
    
    def is_palindrome(self, number):
        num_str = str(number)
        return num_str == num_str[::-1]

complex_calculator = ComplexCalculator()
