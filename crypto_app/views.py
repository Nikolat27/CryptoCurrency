from django.shortcuts import render
from datetime import datetime
from crypto_app.models import Crypto
import requests


# Create your views here.
def price_page(request):
    cryptos = Crypto.objects.all()
    crypto_name = "litecoin"
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}"
    data = requests.get(url)
    json_data = data.json()
    current_price = json_data['market_data']['current_price']['usd']

    return render(request, "crypto_app/price_page.html", context={"cryptos": cryptos
        , "price": current_price})
