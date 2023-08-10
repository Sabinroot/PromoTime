import requests
import time
url_mein_1 = "https://api.promotime.tcl.zendo.cloud/api/v1/login"

url_mein_2 = "https://api.promotime.tcl.zendo.cloud/api/v1/user/finance/accounts"
url_mein_3 = "https://api.promotime.tcl.zendo.cloud/api/v1/shop/carts"
url_mein_4 = "https://api.promotime.tcl.zendo.cloud"
url_mein_5 = "https://api.promotime.tcl.zendo.cloud"

# Выбери пользователя для последовательности действия 1. Авторизауия. 2. Покупка товара. 3. Активация матрици
body_1_username = "test10001"
password = "123456"
headers =  register_headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
        }
# сдесь настройка переменных по счетам .В переменную account_account ставь пермеменную счета которая в себе несет нужное имя счета.
# Так система поймет по какому имени брать id счета.
account_ustd = 'Основной счет USDT'
account_btk = 'Основной счет BTC'
account_account = account_ustd  # настрой переменную
payment_currency_id="10"
# настрой продукта для покупки
product_id = "84"
quantity = "1"

# Настройка бонус аккаунта для активации матриц.
account_bonus_ustd = "Бонусный счет USDT"
account_bonus_btk = 'Бонусный счет BTC'
account_bonus_name = account_bonus_ustd
payment_currency_bonus_id="10"
matrix_num = "1"

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

# Шаг 2. Покупка товара.
        token_1 = post_1.json()['data']['token']
        register_headers_2 = \
            {
            'Authorization': f'Bearer {token_1}',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, /'
            }

        get_1 = requests.get(url=url_mein_2, headers=register_headers_2)
        if get_1.status_code == 200:
            get_1 = get_1.json()
        account_main = None
        for account in get_1['data']:
            if account['name'] == account_account:
                account_main = account['id']   #  account_ustd_main  это переменная которую система использует как номер счета
                break

        print("Шаг 2. Покупка товара.")
        print(account_account,"id", account_main)
        print(" ")
        print("Создаем карзину")
        print(" ")
        post_1 = requests.post(url=url_mein_3, headers=register_headers_2)  # запрос по карзине
        print("Статус код:", str(post_1.status_code))
        print("корзина id = ", str(post_1.json()['data']['id']))  # берем id карзины

        # часть вторая
        # из полученых джейсонн данных достаем id карзины и вставляем в запрос для добавления продукта. олл и id продукта в переменной выше
        item = post_1.json()['data']['id']
        body_1 = {
            "product_id": product_id,
            "quantity": quantity
        }

        url_add_item = "https://api.promotime.tcl.zendo.cloud/api/v1/shop/carts/{}/add-product"
        updated_url = url_add_item.format(item)

        post_2 = requests.post(url=updated_url, headers=register_headers_2, json=body_1)  # запрос на добовление продукта
        print("Товар в корзину добавлен,Статус код:", str(post_2.status_code))


        body_2 = {
            "finance_account_id": account_main,  # ПЕРЕМЕННАЯ ВЫШЕ
            "payment_currency_id": payment_currency_id,
            "recipient_type": "me",
            "payment_type": "account",
            "delivery_country_id": "3572887",
            "delivery_state_id": "3572807",
            "delivery_city_id": "3572772",
            "police_agree": "1",
            "newuser_agree": "1",
            "country_id": "690791",
            "delivery_postcode": "55555",
            "delivery_house": "kknmkl",
            "delivery_street": "kmkmkmd",
            "region_id": "700567",
            "city_id": "700569",
            "do_not_call_back":"1",
            "delivery_type": "DHL"
        }
        url_сheckout = "https://api.promotime.tcl.zendo.cloud/api/v1/shop/carts/{}/checkout"
        updated_url_2 = url_сheckout.format(item)
        post_3 = requests.post(url=updated_url_2, headers=register_headers_2, json=body_2)
        #print(post_3.json())
        print("покупка успешна, статус код:", str(post_3.status_code))
       # print("Вот результат JSON", str(post_3.json()))  # если интересно что приходит в ответе то раскоментируй print/
        print("--------------------------")

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
        print("задержка времени 3 сек.")
        time.sleep(3)
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