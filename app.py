from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Привет! Я Катто</h1>
    <p>Учу Python с нуля каждый день</p>
    <p>Это мой первый сайт на Flask!</p>
"""

@app.route("/about")
def about():
    return """
    <h1>Обо мне</h1>
    <p>Мне 22 года</p>
    <p>Цель - стать программистом</p>
"""

if __name__ == "__main__":
    app.run(debug=True)