from flask import Flask, render_template, url_for
from toh import toh

app = Flask(__name__)


@app.route("/")
def home():
    """home page for app"""
    return f"<h1>Home of the Tower Of Hanoi solver!</h1><p><a href={url_for('toh_solved',disc_count=3)}>Solve TOH for 3 discs!</a></p>"


@app.route("/toh/<int:disc_count>")
def toh_solved(disc_count):
    """"page to solve toh based on passed in number of discs in the url"""
    steps = []
    toh(steps, disc_count, 'A', 'C', 'B')
    return render_template('index.html', count=disc_count, results=steps)
