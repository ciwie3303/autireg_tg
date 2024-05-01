import aiohttp
import asyncio
import json
import time

API_BASE_URL = "https://api.sms-activate.org/stubs/handler_api.php"

async def get_countries(api_key: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_BASE_URL}?api_key={api_key}&action=getCountries") as response:
            response_text = await response.text()
            try:
                countries_data = json.loads(response_text)
            except json.JSONDecodeError:
                print("Ошибка декодирования JSON. Неверный формат ответа.")
                return None

            countries_rus = {}
            print("Список стран:")
            for country_id, country_info in countries_data.items():
                if 'rus' in country_info:
                    country_name = country_info['rus']
                    countries_rus[country_id] = (country_name, country_id) 
                    print(f"ID: {country_id} | {country_name}")  
            
            return countries_rus


async def get_number(api_key: str, service: str, max_price: int, country: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_BASE_URL}?api_key={api_key}&action=getNumber&service={service}&country={country}&maxPrice={max_price}") as response:
            result = await response.text()
            print(result)
            result = result.split(":")
            if result[0] == "ACCESS_NUMBER":
                return result[1]  
            else:
                print("Не удалось получить номер.")
                return None

async def get_status(api_key: str, number_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_BASE_URL}?api_key={api_key}&action=getStatus&id={number_id}") as response:
            return await response.text()

async def main():
    api_key = '2016dfA7389e032ebA02707cceb581cc'
    countries = await get_countries(api_key)
    if not countries:
        print("Не удалось получить список стран. Проверьте ваш API ключ.")
        return

    country_id = "6"
    service = 'tg'
    max_price = '18'

    number_id = await get_number(api_key, service, max_price, country_id)
    if not number_id:
        return

    print("Номер успешно получен. ID номера:", number_id)

    while True:
        status = await get_status(api_key, number_id)
        print("Статус номера:", status)
        if status != "STATUS_WAIT_CODE":
            break
        await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
