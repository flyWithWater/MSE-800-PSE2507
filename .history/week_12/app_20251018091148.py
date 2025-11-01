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



@app.route("/pages_links")
def show_page_with_hyperlink():
    hyper_link = "https://www.google.com"
    img_link = "https://690603e944df7af17495a81475460d7afce03e59.mdnplay.dev/zh-CN/docs/Web/HTML/Reference/Elements/img/clock-demo-400px.png"
    return f"""<html>
    <h1>Title</h1>
    </hr>
        <a href = {hyper_link}>Google's website</a>

        <a href = {img_link}
        <img src={img_link}/></a>

    </html>"""


if __name__ == "__main__":
    app.run(debug=True)


