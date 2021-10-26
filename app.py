from libs.openexchange import OpenExchangeClient

APP_ID = '5e00eba3300b4b11923e4b6c3197503a'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print(f'USD{usd_amount} is GBP{gbp_amount:.2f}')