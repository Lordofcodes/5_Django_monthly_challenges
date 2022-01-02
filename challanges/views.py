from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.


monthly_challenges_dict = {
    "january": "Keep life & work balance.. fluent in DG",
    "february": "0 SHIT FOOD AND FAST FOOD TRAINING 2X/PER WEEK",
    "march": "regular r-vu LIFE & WORK BALANCE",
    "april": "Travel to Italy",
    "may": "regular training GUM AND DIET",
    "june": "City Break UKRAINE",
    "july": "SOPOT 2022 ONLY 4 DAYS",
    "august": "Travel to Scwizrland... 1 week holiday",
    "september": "PYTHONT RAINING EVERYDAY 1 HOUR",
    "october": "REFURBISHMENT OF FLOAT  ",
    "november": "NEW WORK   ",
    "december": "CHILL"
}


def index(request):
    months = list(monthly_challenges_dict.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def january_1(request):
    return HttpResponse("Keep life & work balance.. fluent in DG")  # method not efficient OLD


def february_1(request):
    return HttpResponse("0 SHIT FOOD AND FAST FOOD TRAINING 2X/PER WEEK")  # method not efficient OLD


def monthly_challenges_by_numbers(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid MONTH KURWA")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)  # PRZEKIEROWANIE WAZNE


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month_name": month  # THIS IS RECOMMENDED TO PUT ANY STYLE LOGIC IN VIEWS… SEE TEMPLATES FORMATTING
        })
    except:
        return HttpResponseNotFound("THIS MONTH IS NOT SUPPORTED")
