import os
import django
import requests

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capital_city_game.settings")
django.setup()

from game.models import Country

def populate_countries():
    url = "https://countriesnow.space/api/v0.1/countries/capital"
    response = requests.get(url)
    data = response.json()

    for country_data in data["data"]:
        Country.objects.create(
            name=country_data["name"],
            capital=country_data["capital"]
        )

if __name__ == "__main__":
    populate_countries()
