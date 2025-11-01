
from flask import Flask


app = Flask(__name__)



@app.route("/bmi")
def form_page():
    return f"""
        <html>
            <h1>BMI Calculator</h1>
            <form action="" method="post">
                
            </form>
        </html>

    """




if __name__ == "__main__":
    app.run(debug=True)
