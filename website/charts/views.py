from django.shortcuts import render
from .models import Data
import requests

# Create your views here.


def toEth(wei):
    eth = wei[0:-18] + '.' + wei[-18:-1]
    return eth


def chart(request, chart_name):
    data = Data.objects.all()

    accounts = []

    for i in range(5):
        temp = ""

        for j in range(20):
            temp += data[j+20*i].address + ","

        temp = temp[:-1]
        api = "https://api.etherscan.io/api?module=account&action=balancemulti&address=" + temp + "&tag=latest&apikey=EUR9SA29QNGS3R91RESHMNSQF6B2C8C9MS"
        api_request = requests.get(api)
        data_from_api = api_request.json()
        accounts += data_from_api["result"]

        for j in range(20):
            accounts[j+20*i]['balance'] = float(toEth(accounts[j+20*i]['balance']))



    context = {
        "accounts": accounts,
        "chart": chart_name,
        "index": False
    }

    return render(request, 'chartapp/index.html', context)


def index(request):
    return render(request, 'chartapp/index.html', {"index": True})