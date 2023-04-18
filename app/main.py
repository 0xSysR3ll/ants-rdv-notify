# /usr/bin/env python3
# *-* coding: utf-8 *-*

import time
from datetime import datetime, timedelta
import yaml
import discord
import asyncio
import aiohttp
from colors import *
import requests as req
from geopy.geocoders import Nominatim
import requests_random_user_agent

API_URL = "https://api.rendezvouspasseport.ants.gouv.fr/api/SlotsFromPosition"


class DiscordWebhook():
    """
    Creates a new DiscordWebhook object with the specified webhook URL.

    :param webhook_url: The URL of the Discord webhook.
    :type webhook_url: str
    """

    def __init__(self, webhook_url) -> None:
        self.webhook_url = webhook_url

    async def send_notification(self, embed):
        """
        Sends a notification to the Discord webhook with the specified embed.

        :param embed: The embed to send.
        :type embed: discord.Embed
        :return: None
        """

        # Creating a webhook object
        webhook = discord.Webhook.from_url(
            self.webhook_url, session=aiohttp.ClientSession())
        # Create the payload
        await webhook.send(embed=embed)


def search_rendez_vous(radius_km: int, longitude: float, latitude: float,
                       city: str, reason: str, documents_number: int):
    """
    A function that searches for available rendez-vous slots
    for French national identity cards (CNI) and passports using
    the API provided by the French government.

    :param radius_km: The radius in kilometers around the city.
    :type radius_km: int
    :param longitude: The longitude of the city.
    :type longitude: float
    :param latitude: The latitude of city.
    :type latitude: float
    :param city: The city to search for available rendez-vous slots.
    :type city: str
    :param reason: The reason of the rendez-vous (CNI, PASSPORT, CNI-PASSPORT).
    :type reason: str
    :param documents_number: The number of people wishing for a rendez-vous (1-5).
    :type documents_number: int
    :return: A tuple containing a boolean indicating whether or not
    a rendez-vous slot was found and a list of available rendez-vous slots.
    :rtype: tuple
    """

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
    # Parse config file
    try:
        config = yaml.safe_load(open('config.yml'))
    except Exception as e:
        print(f"{error()} Error while parsing config file: {e}")
        exit(1)
    general = config['general']
    city = general['city']
    reason = general['reason']
    documents_number = general['documents_number']
    radius_km = general['radius_km']
    webhook_url = config['discord']['webhook_url']

    notifier = DiscordWebhook(webhook_url)  # Create a notifier object

    # Get location from city name
    geolocator = Nominatim(user_agent="cni_passport_rdv_finder")
    location = geolocator.geocode(city)

    while True:
        found, places = search_rendez_vous(radius_km=radius_km,
                                           longitude=location.longitude,
                                           latitude=location.latitude,
                                           city=city,
                                           reason=reason,
                                           documents_number=documents_number
                                           )
        if found:
            for place in places:
                rdv_len = len(place['available_slots'])
                print(
                    f"{success()} {rdv_len} créneaux trouvé(s) à la {place['name']} !")
                print(f"{info()} Envoi de la notification...")
                try:
                    rdv_place_url = place['website']
                    req.get(rdv_place_url)
                except Exception as e:
                    print(
                        f"{warning()} Impossible de récupérer le lien du site de la {place['name']}.")
                    rdv_place_url = "https://rendezvouspasseport.ants.gouv.fr"
                try:
                    rdv_place_icon = place['city_logo']
                    req.get(rdv_place_icon)
                except Exception as e:
                    print(
                        f"{warning()} Impossible de récupérer l'icône de la {place['name']}.")
                    rdv_place_icon = "https://guichetcartegrise.com/img/ants.jpg"
                embed = discord.Embed(
                    title=f"{rdv_len} créneaux trouvé(s) à la {place['name']}.",
                    description=f":round_pushpin: Distance : {place['distance_km']} kms",
                    color=discord.Color.red())
                embed.set_author(
                    name=f"{place['name']}",
                    url=rdv_place_url,
                    icon_url=rdv_place_icon
                )
                for rdv in place['available_slots']:
                    rdv_date = datetime.strptime(
                        rdv['datetime'], '%Y-%m-%dT%H:%M:%S+00:00')
                    rdv_day = rdv_date.strftime('%d/%m/%Y')
                    rdv_time = rdv_date.strftime('%H:%M')
                    rdv_link = rdv['callback_url']
                    embed.add_field(
                        name=f":date: Le {rdv_day} à {rdv_time}",
                        value=f":globe_with_meridians: [Prendre rendez-vous]({rdv_link})",
                        inline=False
                    )
            asyncio.run(notifier.send_notification(embed))
        else:
            print(
                f"{info()} Pas de créneaux trouvé. Lancement de la recherche dans 5 minutes...")
        time.sleep(300)


if __name__ == '__main__':
    main()
