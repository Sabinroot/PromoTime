import requests

url_register = "https://api.promotime.tcl.zendo.cloud/api/v1/login"
headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
            }

def register_user():
    body_1_username = "w1000"
    password = "1234561"
    body = {
        "login": body_1_username,
        "password": password
    }

    response = requests.post(url=url_register, headers=headers, json=body)
    assert 422 == response.status_code

    if response.status_code == 200:
        print(response.status_code)
        print("Registration successful.")
        print("Response:", response.text)
    else:
        print("Registration failed.")
        print(response.status_code)
        print("Response:", response.json())

# Send the registration request 5 times with different credentials
for i in range(1000):
    username = f"user_{i}"
    password = f"password_{i}"
    register_user()


