from flask import Flask


app = Flask(__name__)


@app.route("/")
def function():
    return "hello world!"  


@app.route("/fly")
def fly():
    return "<h1>Flying</h1>"

if __name__ == "__main__":
    app.run(debug=True)