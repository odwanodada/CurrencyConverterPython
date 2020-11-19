import requests


# country=ToCurrency_option.get()
url = f'https://v6.exchangerate-api.com/v6/432283c2a5a8200001041f81/latest/USD'

response = requests.get(url)
result = response.json()
print(result)