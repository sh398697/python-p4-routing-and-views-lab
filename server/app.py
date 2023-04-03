#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:my_parameter>')
def print_string(my_parameter):
    print(my_parameter)
    return my_parameter

@app.route('/count/<int:my_int>')
def count(my_int):
    return_string = ''
    for x in range(my_int):
        return_string += str(x)
        return_string += '\n'
    return return_string

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
