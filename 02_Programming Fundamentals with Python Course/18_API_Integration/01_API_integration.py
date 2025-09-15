import requests

def get_price_eur_to_usd():
    url = 'https://www.freeforexapi.com/api/live?pairs=EURUSD'

    try:
        response = requests.get(url)
        date = response.json()
        rate = date['rates']['EURUSD']['rate']
        return rate

    except requests.exceptions.RequestException as e:
        print('Error', e)

current_rate_EURUSD = get_price_eur_to_usd()

eur = float(input('Enter the ammount of Euro you want to exchange: '))
eur_to_usd = eur * current_rate_EURUSD
print(f"{eur} euros are {eur_to_usd} USD!")