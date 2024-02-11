import boto3
from flask import Flask, request, redirect, jsonify
from app.apis.request_utils import send_post

app = Flask(__name__)
app.secret_key = "flask-secret-key"


# Trigger Lambda
def lambda_handler(event, context):
    print(event)
    return "Hello from Lambda!"


# Post the data to database
@app.route("/post_data", methods=["POST"])
def enter_data():
    if request.method == "POST":
        fields = [request.form.get(key) for key in request.form.to_dict()]
        return fields


# Fetch data from database
@app.route("/get_data", methods=["GET"])
def get_data():
    if request.method == "GET":
        fields = [request.form.get(key) for key in request.form.to_dict()]
        return jsonify({"data": fields})


if __name__ == "__main__":
    app.run(debug="True", host="127.0.0.1", port="5001")
