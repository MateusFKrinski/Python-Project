import requests


def connect_and_publish(api_url, data, auth_header=None):

    headers = {}
    if auth_header:
        headers.update(auth_header)

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        return {"status": "success", "data": response.json()}
    else:
        return {"status": "error", "data": {"code": response.status_code, "message": response.text}}


api_url = "https://api.example.com/v2/publications"
data = {}
auth_header = {"Authorization": "Bearer ***Token***"}

response_data = connect_and_publish(api_url, data, auth_header)

if response_data["status"] == "success":
    print("Publication successful!")
else:
    print("Error:", response_data["data"]["message"])
