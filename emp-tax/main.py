from calc import PaymentCalc, TaxCalc
from employees import BazaDanych, Employee
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()



@app.route("/")
def index():
    return 'Hello World!'








if __name__ == "__main__":
    app.run(debug=True)