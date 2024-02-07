from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import magic
import os

SK = "Test Key Map Legend"
FILE_EXT = ".csv"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "websol/tmp_file/uploads"
app.secret_key = SK


@app.route("/", methods=["GET", "POST"])
def root_page():
    if request.method == "POST":
        return "Success"
    return "Root Page"


@app.route("/compare_files", methods=["GET", "POST"])
def compare_files():
    if request.method == "POST":
        if "file_a" not in request.files or "file_b" not in request.files:
            return "no file"

        file_a = request.files["file_a"]
        file_b = request.files["file_b"]

    
        if file_a.filename == "" or file_b.filename == "":
            return "Please select two files to compare."

       
        if not file_a.filename.endswith(".csv") or not file_b.filename.endswith(".csv"):
            return "Please upload CSV files only."

        files = [file_a, file_b]
        statuses = []
        for file in files:
            if validate_files(file=file):
                statuses.append("True")
            else:
                statuses.append("False")

        STATUS = statuses
        if STATUS[0] and STATUS[1]:
            file_a.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"], secure_filename(file_a.filename)
                )
            )
            file_b.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"], secure_filename(file_b.filename)
                )
            )

        return "Files uploading locally"

    return render_template("compare_files.html")


def validate_files(file):
    try:
        _mime = magic.Magic(mime=True).from_buffer(file.read())
        if not _mime == "text/csv":
            print("not a csv")
        status = True
    except Exception as e:
        status = False
        print("File content unknown")
    finally:
        file.seek(0)

    return status


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")
