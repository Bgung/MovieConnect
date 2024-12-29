import os
import flask

app = flask.Flask(__name__)

data_person = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 40},
    {'name': 'Eve', 'age': 45},
    {'name': 'Frank', 'age': 50},
    {'name': 'Grace', 'age': 55},
    {'name': 'Heidi', 'age': 60},
    {'name': 'Ivan', 'age': 65},
    {'name': 'Judy', 'age': 70},
    {'name': 'Kevin', 'age': 75},
    {'name': 'Lily', 'age': 80},
    {'name': 'Mary', 'age': 85},
    {'name': 'Nancy', 'age': 90},
    {'name': 'Oliver', 'age': 95},
    {'name': 'Peter', 'age': 100},
    {'name': 'Quincy', 'age': 105},
    {'name': 'Robert', 'age': 110},
    {'name': 'Sarah', 'age': 115},
    {'name': 'Tom', 'age': 120},
]

movies = [
    {'name': 'The Shawshank Redemption', 'year': 1994},
    {'name': 'The Godfather', 'year': 1972},
    {'name': 'The Dark Knight', 'year': 2008},
]

@app.route('/')
def index():
    return flask.render_template(
        "index.html", data=data_person
    )

@app.route('/movie')
def movie():
    return flask.render_template("movie.html", data=movies)

if __name__ == '__main__':
    app.run(debug=True)

