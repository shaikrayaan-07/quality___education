
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/planner')
def planner():
    return render_template('planner.html')

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

@app.route('/skillshare')
def skillshare():
    return render_template('skillshare.html')

if __name__ == '__main__':
    app.run(debug=True)
