import requests
import json

# def Exchange():
    # api data
api_key = "fca_live_ogJxXv67H3cCnm5GHHyhvcjNs4aFHhIdwB1BCin7"

url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"

response = requests.get(url)

data = response.json()

#moneyData = json.dumps(data)

# for clave, valor in moneyData["data"].items():
#     print(f"Clave: {clave},      Valor: {valor}")

print(data['data'])






# "USD"
# "AUD"
# "CAD"
# "EUR"
# "GBP"
# "JPY"
# "MXN"

