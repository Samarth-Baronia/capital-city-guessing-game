# game/views.py
from django.shortcuts import render
from .models import Country
import random

def index(request):
    countries = Country.objects.all()
    random_country = random.choice(countries)

    context = {
        'country': random_country,
    }
    return render(request, 'game/index.html', context)

def check_answer(request):
    if request.method == 'POST':
        country_id = request.POST.get('country_id')
        user_guess = request.POST.get('user_guess')
        country = Country.objects.get(pk=country_id)

        if user_guess.lower() == country.capital.lower():
            message = 'Correct!'
        else:
            message = 'Incorrect. The correct answer is ' + country.capital

        return render(request, 'game/result.html', {'message': message})
