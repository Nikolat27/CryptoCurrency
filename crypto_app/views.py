from django.shortcuts import render
from crypto_app.models import Crypto
import requests


# Create your views here.
def price_page(request):
    crypto_name = request.GET.get("currency")
    print(crypto_name)
    if crypto_name:
        cryptos = Crypto.objects.all()
        url = f"https://api.coingecko.com/api/v3/coins/{crypto_name}"
        data = requests.get(url)
        json_data = data.json()
        current_price = json_data['market_data']['current_price']['usd']
        context = {"cryptos": cryptos, "price": current_price}
    else:
        cryptos = Crypto.objects.all()
        context = {"cryptos": cryptos}

    return render(request, "crypto_app/price_page.html", context=context)
