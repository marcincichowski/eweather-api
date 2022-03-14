import datetime
import sys

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore

from eweather_api_controller.models import Place
from eweather_api_controller.serializers import PlaceWeatherInfoSerializer

openweathermap = {
    'url': 'https://api.openweathermap.org/data/2.5/weather',
    'key': 'f28aad6ea97881fd19059ac3f5f6ae93'
}


def fetch_places_info():
    places = Place.objects.all()

    for place in places:
        print(f'Attempting to fetch weather info for ({place.lat}|{place.lon})')

        try:
            request_url = f'{openweathermap["url"]}?' \
                          f'lat={place.lat}&' \
                          f'lon={place.lon}&' \
                          f'appid={openweathermap["key"]}&' \
                          f'units=metric'

            response = requests.get(request_url).json()

            data = {
                'lat': place.lat,
                'lon': place.lon,
                'temperature': response['main']['temp'],
                'pressure': response['main']['pressure'],
                'humidity': response['main']['humidity'],
                'timestamp': datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
            }

            serializer = PlaceWeatherInfoSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                print(f'Saved to database.')

        except Exception as err:
            print(f'An error has occurred:')
            print(err)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    #scheduler.add_job(id='fetch_places_info',
    #                  name='Fetching hourly weather info about every place from database.',
    #                  func=fetch_places_info,
    #                  trigger=CronTrigger(
    #                      minute="00"
    #                  ),
    #                  jobstore='default',
    #                  replace_existing=True)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
