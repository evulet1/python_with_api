import requests

APP_ID = '5e00eba3300b4b11923e4b6c3197503a'
ENDPINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f'{ENDPINT}?app_id={APP_ID}')
exchange_rates = response.json()['rates']

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['GBP']

print(f'USD{usd_amount} is GBP{gbp_amount}')