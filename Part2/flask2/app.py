from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/')
def randomnumber():
    num1 = random.randint(1, 10000)
    num2 = random.randint(1, 10000)
    math = num1 + num2
    return f'Math Equation: {num1} + {num2} = {math}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')