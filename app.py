import time
from libs.openexchange import OpenExchangeClient

APP_ID = '5e00eba3300b4b11923e4b6c3197503a'

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
end = time.time()
print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
end = time.time()
print(end-start)

start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
end = time.time()
print(end-start)


print(f'USD{usd_amount} is GBP{gbp_amount:.2f}')

