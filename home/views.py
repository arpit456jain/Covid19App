from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def home(request):
        url = f'https://api.covid19api.com/summary'
        r = requests.get(url)
        data = r.json()
        # print(data,type(data))
        # print(data['location'])
        payload = {
            "NewConfirmed" : data["Global"]["NewConfirmed"],
            "TotalConfirmed" : data["Global"]["TotalConfirmed"],
            "NewDeaths" : data["Global"]["NewDeaths"],
            "TotalDeaths" : data["Global"]["TotalDeaths"],
            "Countries"  : data["Countries"],
        }
        
        # print(payload)
        return render(request,'home.html',payload)