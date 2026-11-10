import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXCHANGE_RATE_API_KEY")
currency = "KES"

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rates = data["conversion_rates"]
    print(f"Exchange rates for {currency}:")
    for target_currency, rate in rates.items():
        print(f"{target_currency}: {rate}")

elif response.status_code == 401:
    print("API key is invalid or not yet active. Check your .env file.")

elif response.status_code == 404:
    print(f"Currency not found: {currency}. Check the currency code.")

elif response.status_code == 429:
    print("Too many requests. Wait before trying again.")

else:
    print(f"Unexpected error: {response.status_code}")
    print(response.text)