from django.shortcuts import render
from crypto_app.models import Crypto
import requests as requests_package


# Create your views here.

def cryptoPrice_inquiry(request, crypto, currency):  # I use this function for inquiry the selected crypto
    inquiry = f"https://api.coingecko.com/api/v3/coins/{crypto}"  # coingecko website api for inquiring the crpyto
    inquiry_data = requests_package.get(inquiry)  # using REQUESTS package to send the request
    json_data = inquiry_data.json()  # creating a new variable and put that data with serializing it with .json() module
    current_price = json_data['market_data']['current_price'][
        f'{currency}']  # finding the crypto with considered currency
    return current_price  # Conclusion


def price_page(request):
    crypto = request.GET.get("crypto")
    currency = request.GET.get("currency")
    if crypto and currency:
        cryptos = Crypto.objects.all()
        # url = f"https://api.coingecko.com/api/v3/coins/{crypto}"
        # data = requests.get(url)
        # json_data = data.json()
        # current_price = json_data['market_data']['current_price'][f'{currency}']
        current_price = cryptoPrice_inquiry(request, crypto, currency)
        context = {"cryptos": cryptos, "price": current_price}
    else:
        cryptos = Crypto.objects.all()
        context = {"cryptos": cryptos}
    return render(request, "crypto_app/price_page.html", context=context)


def convert_page(request):
    currencies = Crypto.objects.all()  # Our cryptos and currencies
    firstCrypto = request.GET.get("firstCrypto")
    amount = request.GET.get("amount")
    secondCrypto = request.GET.get("secondCrypto")
    currency = request.GET.get("currency")

    if firstCrypto and secondCrypto and currency and amount:
        currencies = Crypto.objects.all()  # Our cryptos and currencies
        firstCrypto_price = cryptoPrice_inquiry(request, firstCrypto, currency)  # First we get our first crypto price
        secondCrypto_price = cryptoPrice_inquiry(request, secondCrypto,
                                                 currency)  # Second we get our second crypto price
        crypto_prices = float(firstCrypto_price) / float(
            secondCrypto_price)  # Third we Divide them and put them in a variable
        final_price = float(
            amount) * crypto_prices  # Then we multiply our user considered amount to the previous variable
        context = {"currencies": currencies, "price": final_price}
    else:
        context = {"currencies": currencies}

    return render(request, "crypto_app/convert_page.html", context=context)
