import boto3
from flask import Flask, request, redirect

app = Flask(__name__)


# Trigger Lambda
def lambda_handler(event, context):
    print(event)
    return "Hello from Lambda!"


# Post the data to database
@app.route("/post_data", methods=["GET", "POST"])
def enter_data():
    if request.method == "POST":
        new_data = request.get_json()
        return new_data
    return "GET method"


# Fetch data from database
@app.route("/get_data", methods=["GET"])
def get_data():
    return "GET method"


if __name__ == "__main__":
    app.run(debug="True", host="127.0.0.1", port="5000")
