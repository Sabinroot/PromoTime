import requests

url_mein_1 = "https://api.promotime.tcl.zendo.cloud/api/v1/login"

url_mein_2 = "https://api.promotime.tcl.zendo.cloud/api/v1/user/finance/accounts"
url_mein_3 = "https://api.promotime.tcl.zendo.cloud/api/v1/shop/carts"
url_mein_4 = "https://api.promotime.tcl.zendo.cloud"
url_mein_5 = "https://api.promotime.tcl.zendo.cloud"

# Выбери пользователя для последовательности действия 1. Авторизауия. 2. Покупка товара. 3. Активация матрици
body_1_username = "q10012"
password = "123456"
headers =  register_headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
        }



# Настройка бонус аккаунта для активации матриц.
account_bonus_ustd = "Бонусный счет USDT"
account_bonus_btk = 'Бонусный счет BTC'
account_bonus_name = account_bonus_btk
payment_currency_bonus_id="12"
matrix_num = "5"

class Methods_1(): # короче мин. значения

    def __init__(self):
        pass

    def step_1(self):

        body_1 = {

            "login": body_1_username,
            "password": password
        }
# Шаг 1. Авторизация.
        print("Шаг 1. Авторизация юзера для покупки и открытия платформы матриц")
        post_1 = requests.post(url=url_mein_1, headers=register_headers, json=body_1)
        assert 200 == post_1.status_code
        if post_1.status_code == 200:
            print("статус код =", post_1.status_code)
            print("------------")
        else:
            print("case is not working")


        token_1 = post_1.json()['data']['token']
        register_headers_2 = \
            {
            'Authorization': f'Bearer {token_1}',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
            }


        print("Активируем матрицу.")
        get_2 = requests.get(url=url_mein_2, headers=register_headers_2)
        if get_2.status_code == 200:
            get_2 = get_2.json()
        account_bonus = None
        for account in get_2['data']:
            if account['name'] == account_bonus_name:
                account_bonus = account['id']  #
                break
        print(account_bonus_name,"id", account_bonus)
        print(" ")
        url_add_item_2 = "https://api.promotime.tcl.zendo.cloud/api/v1/user/matrix/{}/activate"
        updated_url_3 = url_add_item_2.format(matrix_num)
        body_4 = {
            "finance_account_id": account_bonus,
            "finance_password": password,
            "finance_currency_id": payment_currency_bonus_id
        }
        post_4 = requests.post(url=updated_url_3, headers=register_headers_2, json=body_4)
        print (post_4.json())
        print(post_4.status_code)



case_1 = Methods_1()
case_1.step_1()