from flask import Flask, render_template
import csv

app = Flask(__name__)

def read_ditiss_data():
    locker_data = []
    with open('./student_allocation_data/ditiss.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            locker_data.append(row)
    return locker_data

def read_dac_data():
    locker_data = []
    with open('./student_allocation_data/dac.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            locker_data.append(row)
    return locker_data

def read_desd_data():
    locker_data = []
    with open('./student_allocation_data/desd.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            locker_data.append(row)
    return locker_data


def read_dmc_data():
    locker_data = []
    with open('./student_allocation_data/dmc.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            locker_data.append(row)
    return locker_data

def read_dbda_data():
    locker_data = []
    with open('./student_allocation_data/dbda.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            locker_data.append(row)
    return locker_data


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/ditiss')
def ditiss():
    locker_data = read_ditiss_data()
    return render_template('ditiss.html', locker_data=locker_data)

@app.route('/dac')
def dac():
    locker_data = read_dac_data()
    return render_template('dac.html', locker_data=locker_data)

@app.route('/desd')
def desd():
    locker_data = read_dac_data()
    return render_template('desd.html', locker_data=locker_data)

@app.route('/dmc')
def dmc():
    locker_data = read_dac_data()
    return render_template('dmc.html', locker_data=locker_data)

@app.route('/dbda')
def dbda():
    locker_data = read_dac_data()
    return render_template('dbda.html', locker_data=locker_data)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
