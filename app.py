from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    imya = request.form["imya"]
    return f"<h1>Привет, {imya}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)