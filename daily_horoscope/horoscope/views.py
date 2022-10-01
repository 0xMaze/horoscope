from django.shortcuts import render
from django.http import HttpResponse
from .models import Horoscope
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    return render(request, "horoscope/index.html")


def horoscope(request):
    sign = request.GET.get("sign")

    sign_dict = {
        "Aries": "1",
        "Taurus": "2",
        "Gemini": "3",
        "Cancer": "4",
        "Leo": "5",
        "Virgo": "6",
        "Libra": "7",
        "Scorpio": "8",
        "Sagittarius": "9",
        "Capricorn": "10",
        "Aquarius": "11",
        "Pisces": "12",
    }

    url = (
        "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="
        + sign_dict[sign]
    )

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    content = soup.find("div", class_="main-horoscope")
    horoscope = content.find("p").text[14::]
    date = content.find("strong").text

    context = {
        "horoscope": horoscope,
        "date": date,
        "sign": sign,
    }
    return render(request, "horoscope/horoscope_page.html", context)
