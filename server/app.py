#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    num = '\n'.join(str(i) for i in range(parameter))
    return f"{num}\n"
          
    
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    result = None
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1/num2
    elif operation == '%':
        result = num1%num2    
        
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5005, debug=True)