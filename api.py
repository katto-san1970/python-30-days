import requests

try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()

    print("=== КОНВЕРТЕР ВАЛЮТ ===")
    summa = float(input("Введите сумму в долларах: "))

    print(f"\n{summa} USD = ")
    print(f"        {round(summa * data['rates']["RUB"], 2)} RUB")
    print(f"        {round(summa * data['rates']["EUR"], 2)} EUR")
    print(f"        {round(summa * data['rates']["TRY"], 2)} TRY")

except requests.ConnectionError:
    print("ОШИБКА!!! Нет подключения к интернету.")
except ValueError:
    print("ОШИБКА!!! Введи число.")