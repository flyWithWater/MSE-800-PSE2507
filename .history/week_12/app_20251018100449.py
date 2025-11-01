from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# --- config ---
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def function():
    return "hello world!"

@app.route("/fly")
def fly():
    return "<h1>Flying</h1>"

@app.route("/gender/<gender>")
def variableFunction(gender:str):
    return f"""
        <div>
            <h1>{gender}</h1> is great!!!!
        </div>
    """

@app.route("/cal/<int:number>")
def show_square(number:int):
    return f"the square of {number} is {number**2}"

@app.route("/pages_links")
def show_page_with_hyperlink():
    hyper_link = "https://www.google.com"
    img_link = "https://239da270-4ec4-4d29-bb7e-eaae67aed394.mdnplay.dev/shared-assets/images/examples/grapefruit-slice.jpg"

    return f"""<html>
    <h1>Title</h1>
    <hr>
        <a href="{hyper_link}">Google's website</a>
        <br/><br/>
        <img src="{img_link}" alt="Sample" width="240"/>
        <hr>

        <h3>Upload an image</h3>
        <form action="{url_for('upload_image')}" method="post" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required>
            <button type="submit">Upload</button>
        </form>
    </html>"""

@app.route("/upload_image", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if not file or file.filename == "":
        return "No file selected", 400

    filename = secure_filename(file.filename)
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)

    return redirect(url_for("preview", filename=filename))

@app.route("/preview/<path:filename>")
def preview(filename):
    return render_template_string("""
    <h3>Uploaded image</h3>
    <img src="{{ url_for('uploaded_file', filename=filename) }}" alt="uploaded" style="max-width:480px;">
    <p><a href="{{ url_for('show_page_with_hyperlink') }}">Upload another</a></p>
    """, filename=filename)

# NEW: serve files from /uploads
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
