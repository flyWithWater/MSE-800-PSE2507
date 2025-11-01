
from flask import Flask,url_for
from flask import Blueprint,request,render_template_string


bmi = Blueprint('bmi', __name__, url_prefix='/bmi')



@bmi.route("/")
def form_page():
    return render_template_string(f"""
        <html>
            <h1>BMI Calculator</h1>
            <form action="{url_for('bmi.calculate')}" method="post">
               <div><label for="weight">weight in kg</label><input type="text" name="weight" required /></div> 
                <div><label for="height">height in meters</label><input type="text" name="height" required /></div>
                 <button type="submit">submit</button>
            </form>
            <br/>
            <details>
            <summary>BMI calculate Result</summary>
            
            </details>

        </html>

    """)


@bmi.route("calculate")
def calculate():

    return render_template_string(f"""

""")

 