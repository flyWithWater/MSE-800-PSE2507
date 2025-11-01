
from flask import Flask,url_for
from flask import Blueprint,request,render_template_string


user_bp = Blueprint('bmi', __name__, url_prefix='/bmi')



@app.route("/")
def form_page():
    return f"""
        <html>
            <h1>BMI Calculator</h1>
            <form action="{url_for('submit_information')}" method="post">
               <div><label for="weight">weight in kg</label><input type="text" name="weight" required /></div> 
                <div><label for="height">height in meters</label><input type="text" name="height" required /></div>
                 <button type="submit">submit</button>
            </form>
            <br/>
            <details>
            <summary>BMI calculate Result</summary>
            
            </details>

        </html>

    """




if __name__ == "__main__":
    app.run(debug=True)
