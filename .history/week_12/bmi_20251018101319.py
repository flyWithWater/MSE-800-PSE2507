
from flask import Flask


app = Flask(__name__)



@app.route("/bmi")
def form_page():
    return f"""
        

    """




if __name__ == "__main__":
    app.run(debug=True)
