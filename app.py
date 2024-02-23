from flask import Flask, render_template
import csv

app = Flask(__name__)

def read_locker_data():
    locker_data = []
    with open('./data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            locker_data.append(row)
    return locker_data

@app.route('/')
def index():
    locker_data = read_locker_data()
    return render_template('index.html', locker_data=locker_data)

if __name__ == '__main__':
    app.run(debug=True)
