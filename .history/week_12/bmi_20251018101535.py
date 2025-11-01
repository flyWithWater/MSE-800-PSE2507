
from flask import Flask,url_for


app = Flask(__name__)



@app.route("/bmi")
def form_page():
    return f"""
        <html>
            <h1>BMI Calculator</h1>
            <form action="{url_for('submit_information')}" method="post">

            </form>
        </html>

    """




if __name__ == "__main__":
    app.run(debug=True)
