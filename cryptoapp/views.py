from django.shortcuts import render
from django.http import HttpResponse
import requests 
import json

# Create your views here.
def index(request):
        
        #grab crypto price data

        price_request=requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX &tsyms=USD,EUR')
        price = json.loads(price_request.content)
        
        
        #grab 
        api_request=requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
        api = json.loads(api_request.content)
        return render(request, 'index.html', {"api": api,"price":price})




def prices(request):
        if request.method == 'POST':
                import requests 
                import json 
                
                quote=request.POST['quote']
                quote =quote.upper()
                crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="  + quote +   "&tsyms=USD")
                crypto=json.loads(crypto_request.content)
                
                return render(request,'prices.html',{'quotes':quote,'crypto':crypto})
        
        
        else:
                notfound="entcrypto currency symbol into from above"
                return render(request,'prices.html',{'notfound':notfound})  
        
        
