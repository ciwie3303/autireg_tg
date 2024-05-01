import requests
import json
import time

API_BASE_URL = "https://api.sms-activate.org/stubs/handler_api.php"


def get_countries(api_key: str):
    response = requests.post(f"{API_BASE_URL}?api_key={api_key}&action=getCountries")
    countries_data = json.loads(response.text)
    
    countries_rus = {}
    print("Список стран:")
    for country_id, country_info in countries_data.items():
        if 'rus' in country_info:
            country_name = country_info['rus']
            countries_rus[country_id] = country_name
            print(country_name)
    
    return countries_rus


def get_number(api_key: str, service: str, max_price: int, country: int):
    response = requests.post(f"{API_BASE_URL}?api_key={api_key}&action=getNumber&service={service}&country={country}&maxPrice={max_price}")
    result = response.text.split(":")
    print(result)
    if result[0] == "ACCESS_NUMBER":
        return result[1] 
    else:
        print("Не удалось получить номер.")
        return None


def get_status(api_key: str, number_id: int):
    response = requests.post(f"{API_BASE_URL}?api_key={api_key}&action=getStatus&id={number_id}")
    return response.text


def main():
    api_key = '2016dfA7389e032ebA02707cceb581cc'
    countries = get_countries(api_key)
    if not countries:
        print("Не удалось получить список стран. Проверьте ваш API ключ.")
        return

    country_id = "6"
    service = 'tg'
    max_price = '18'

    number_id = get_number(api_key, service, max_price, country_id)
    if not number_id:
        return

    print("Номер успешно получен. ID номера:", number_id)

    while True:
        status = get_status(api_key, number_id)
        print("Статус номера:", status)
        if status != "STATUS_WAIT_CODE":
            break
        time.sleep(30)


if __name__ == "__main__":
    main()



