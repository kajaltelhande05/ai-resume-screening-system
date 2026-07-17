from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return "No file selected"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

    return render_template(
        "result.html",
        filename=file.filename,
        score="85%"
    )

if __name__ == "__main__":
    app.run(debug=True)
