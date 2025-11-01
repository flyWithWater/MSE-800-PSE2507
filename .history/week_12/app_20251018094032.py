
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string

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



@app.route("/pages_links")
def show_page_with_hyperlink():
    hyper_link = "https://www.google.com"
    img_link = "https://239da270-4ec4-4d29-bb7e-eaae67aed394.mdnplay.dev/shared-assets/images/examples/grapefruit-slice.jpg"
    return f"""<html>
    <h1>Title</h1>
    </hr>
        <a href = "{hyper_link}">Google's website</a>
        <br/>
        
        <form action="/upload_image" method="post" class="form-example" >
        
        <input  type="file" id="name" name="image_uploaded" required    />

        <input type="submit" value="upload" />
        </form>



        

    </html>"""


@app.route("/upload_image",methods=['POST'])
def upload_image():
    inputstream = request.form.get("image_uploaded")
    print(type(inputstream))



if __name__ == "__main__":
    app.run(debug=True)


