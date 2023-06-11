# /usr/bin/env python3
# *-* coding: utf-8 *-*

import time
from datetime import datetime, timedelta
import discord
import asyncio
from colors import *
import requests as req
from geopy.geocoders import Nominatim
import requests_random_user_agent
from notifiers import DiscordWebhook, Telegram
from config import Config

API_URL = "https://api.rendezvouspasseport.ants.gouv.fr/api/SlotsFromPosition"


def search_rendez_vous(radius_km: int, longitude: float, latitude: float,
                       city: str, reason: str, documents_number: int):

    start_date = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
    req_params = {
        "longitude": longitude,
        "latitude": latitude,
        "start_date": start_date,
        "end_date": end_date,
        "radius_km": radius_km,
        "address": city,
        "reason": reason,
        "documents_number": documents_number
    }
    s = req.Session()
    search_results = s.get(url=API_URL, params=req_params).json()
    if len(search_results) > 0:
        return True, search_results
    else:
        return False, None


def main():
    # Load the configuration
    config = Config('config/config.yml')
    config.load()
    city = config.get_config('general', 'city')
    reason = config.get_config('general', 'reason')
    documents_number = config.get_config('general', 'documents_number')
    radius_km = config.get_config('general', 'radius_km')
    notifier_types = config.get_config('notifiers')
    notifiers = []
    for notifier_type in notifier_types:
        if notifier_type == 'discord':
            webhook_url = config.get_config('discord', 'webhook_url')
            notifier = DiscordWebhook(webhook_url)  # Create a notifier object
            notifiers.append(notifier)
        if notifier_type == 'telegram':
            api_id = config.get_config('telegram', 'api_id')
            api_hash = config.get_config('telegram', 'api_hash')
            channel_id = config.get_config('telegram', 'channel_id')
            # Create a notifier object
            notifier = Telegram(api_id, api_hash, channel_id)
            notifiers.append(notifier)

    # Get location from city name
    geolocator = Nominatim(user_agent="cni_passport_rdv_finder")
    location = geolocator.geocode(city)
    print(f"{info()} Recherche de créneaux à {city} et ses environs ({radius_km} kms)...")
    while True:
        found, places = search_rendez_vous(radius_km=radius_km,
                                           longitude=location.longitude,
                                           latitude=location.latitude,
                                           city=city,
                                           reason=reason,
                                           documents_number=documents_number)
        if found:
            loop = asyncio.get_event_loop()
            for notifier in notifiers:
                message = notifier.create_message(places)
                if isinstance(notifier, DiscordWebhook):
                    asyncio.run(notifier.send(message))
                else:
                    loop.run_until_complete(notifier.send(message))
            else:
                print(
                    f"{info()} Pas de créneaux trouvé. Lancement de la recherche dans 5 minutes...")
        time.sleep(300)


if __name__ == '__main__':
    main()
