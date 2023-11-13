from flask import Flask, render_template, request, redirect, url_for
from tools.numbers import simp, comp
from tools.col import zip_names

app = Flask(__name__)

result_calculate = None
result_sum_of_digits = None
result_palindrome = None
result_combine_names = None  # Initialize result_combine_names
calculate_used = False

@app.route('/')
def index():
    return render_template('index.html', result_calculate=result_calculate, result_sum_of_digits=result_sum_of_digits, result_palindrome=result_palindrome, calculate_used=calculate_used, result_combine_names=result_combine_names)

@app.route('/calculate', methods=['POST'])
def calculate():
    global result_calculate, calculate_used
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']

    simple_calculator = simp.SimpleCalculator()

    if operation == 'add':
        simple_calculator.add(num1, num2)
        result_calculate = f"Result of {num1} + {num2}: {simple_calculator.result}"
    elif operation == 'subtract':
        simple_calculator.subtract(num1, num2)
        result_calculate = f"Result of {num1} - {num2}: {simple_calculator.result}"
    else:
        result_calculate = None

    calculate_used = True
    return redirect(url_for('index'))

@app.route('/calculate_comp', methods=['POST'])
def calculate_comp():
    global result_sum_of_digits, calculate_used
    if calculate_used == False:
        result_sum_of_digits = "Must use the calculator at least once to sum digits."
        return redirect(url_for('index'))

    num_to_sum = request.form.get('num_to_sum')

    if num_to_sum:
        try:
            num_to_sum = int(num_to_sum)
            if num_to_sum >= 10:
                complex_calculator = comp.ComplexCalculator()
                digit_sum = complex_calculator.sum_of_digits(num_to_sum)
                result_sum_of_digits = f"Sum of digits of {num_to_sum}: {digit_sum}"
            else:
                result_sum_of_digits = "Please enter a number with at least 2 digits."
        except ValueError:
            result_sum_of_digits = "Invalid input. Please enter a valid number."
    else:
        result_sum_of_digits = None

    return redirect(url_for('index'))

@app.route('/check_palindrome', methods=['POST'])
def check_palindrome():
    global result_palindrome, calculate_used
    if calculate_used == False:
        result_palindrome = "Must use the calculator at least once to check for palindromes."  # Redirect to the index page if calculate hasn't been used
        return redirect(url_for('index'))

    num_to_check = request.form.get('num_to_check')

    if num_to_check:
        try:
            num_to_check = int(num_to_check)
            num_str = str(num_to_check)

            if num_str == num_str[::-1]:
                result_palindrome = f"{num_to_check} is a palindrome!"
            else:
                result_palindrome = f"{num_to_check} is not a palindrome."
        except ValueError:
            result_palindrome = "Invalid input. Please enter a valid number."
    else:
        result_palindrome = None

    return redirect(url_for('index'))

@app.route('/combine_names', methods=['POST'])
def combine_names():
    global result_combine_names
    first_name = request.form.getlist('first_name')  # Get a list of first names
    last_name = request.form.getlist('last_name')    # Get a list of last names

    if first_name and last_name:
        combined_names = zip_names(first_name, last_name)  # Use the zip_names function
        result_combine_names = f"{', '.join(combined_names)}"
    else:
        result_combine_names = "Please enter both first names and last names."

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
