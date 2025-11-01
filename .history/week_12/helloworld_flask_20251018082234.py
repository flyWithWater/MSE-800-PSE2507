from flask import Flask


app = Flask("/")


@app.route("")
def function():
    return "hello world!"  

