import requests
# создание юзеров.
url = "https://api.promotime.tcl.zendo.cloud/api/v1/register"
register_headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, /',
}

inviter = "test1000"   # укажи понсора.


class UserGenerator:  # Гениратор пользователей. Нужно настраивать
    def generate_login(self, index):
        return "test1000" + str(1 + index) #настрой окончание  логина

    def generate_users(self, count):
        for i in range(count):
            login = self.generate_login(i)
            self.create_user(login)

    def create_user(self, login):
        data = {
            "password": "123456",
            "username": login,
            "sponsor_username": inviter,
            'password_confirmation':"123456",
            "email": login + "@gmail.com",
            "agreement": "true",
            "has_sponsor": 1
        }
        response = requests.post(url=url, headers=register_headers, json=data)
        if response.status_code == 201:
            print(f"User {login} created successfully")
            print(response.status_code)
            print(response.json())
            print(login + "@.com")
        else:
            print(f"Failed to create user {login}")
            print(response.status_code)
            print(response.json())


# Использование класса UserGenerator для создания 10 пользователей
generator = UserGenerator()
generator.generate_users(14)