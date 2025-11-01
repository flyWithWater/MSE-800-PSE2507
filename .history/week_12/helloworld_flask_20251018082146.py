import flask from Flask


app = Flask("/")


@app.route("")
def function():
    return "hello world!"

