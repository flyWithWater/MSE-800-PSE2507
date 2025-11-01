from flask import Flask


app = Flask(__name__)


@app.route("/")
def function():
    return "hello world!"  


@app.route("/fly")
def fly():
    return "<h1>Flying</h1>"


@app.route("/gender/<gender>")
def variableFunction(gender:str):
    return  f"""
        <div>
            <h1>{gender}</h1> is great!!!!
        </div>
    """

@app.route("/cal/<int:number>")
def show_square(number:int):
    return f"the squre of {number} is {number**2}"



if __name__ == "__main__":
    app.run(debug=True)


