
from flask import Flask,url_for
from flask import Blueprint,request,render_template_string


bmi = Blueprint('bmi', __name__, url_prefix='/bmi')




@bmi.route("/bmi", methods=["POST", "GET"])
def calculate():
    bmi_result = None
    if request.method=="POST":
        weight_kg_str = request.form.get("weight")
        height_meter_str = request.form.get("height")

        if weight_kg_str is None or height_meter_str is None:
            return render_template_string("No enought Parameter!")
        
        weight_kg = float(weight_kg_str)
        height_meter = float(height_meter_str)

        bmi_result = weight_kg/(height_meter**2)

    return render_template_string("""
        <html>
            <h1>BMI Calculator</h1>
            <form action="{url_for('bmi.calculate')}" method="post">
               <div><label for="weight">weight in kg</label><input type="text" name="weight" required /></div> 
               <br/>
                <div><label for="height">height in meters</label><input type="text" name="height" required /></div>
                 <button type="submit">submit</button>
            </form>
            <br/>
            <details>
            <summary>BMI calculate Result</summary>
            <br/>
            
            </details>
            {% if bmi_result %}
            {bmi_result}
            {% endif %}
        </html>

    """,bmi_result = bmi_result)
 