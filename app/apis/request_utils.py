import requests

POST_URL = "http://localhost:5001/post_data"
GET_URL = "http://localhost:5001/get_data"

VERIFY = False


def send_get(data):
    response = requests.get(url=GET_URL, data=data, verify=False)
    print(f"{response.status_code}\n{response.content}\n{response.text}")
    return response


def send_post(data):
    response = requests.post(url=POST_URL, data=data, verify=False)
    print(f"{response.status_code}\n{response.content}\n{response.text}")
    return response


if __name__ == "__main__":
    data = {"user": "data", "data": "userdata", "unexpected": "unexpected_data"}
    send_post(data=data)
    send_get(data=data)
