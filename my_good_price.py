import requests

# Function which send SMS to user
def inform_me(price):
    API_key = '**********' #Enter API key
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' %API_key
    payload = {'receptor': '', 'message': '$BTC price is as low as %i' %price} #Define receptor number and message 
    response = requests.post(url, data=payload)
    print(response)

# Check price from coinbase  
response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
price = float(response.json()['data']['amount'])

# Driver code 
my_good_price = int(input("Enter you good price: "))

if price <= my_good_price:
    inform_me(price)

input("Press enter to exit")
