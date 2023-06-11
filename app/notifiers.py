import discord
import aiohttp
from colors import *
from datetime import datetime
import asyncio
import requests as req
from telethon import TelegramClient, events, sync


class DiscordWebhook():
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url

    def create_message(self, places):
        for place in places:
            rdv_len = len(place['available_slots'])
            print(
                f"{success()} {rdv_len} créneaux trouvé(s) à la {place['name']} !")
            print(f"{info()} Envoi de la notification sur Discord ...")
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

            message = discord.Embed(
                title=f"{rdv_len} créneaux trouvé(s) à la {place['name']}.",
                description=f":round_pushpin: Distance : {place['distance_km']} kms",
                color=discord.Color.red())
            message.set_author(
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
                message.add_field(
                    name=f":date: Le {rdv_day} à {rdv_time}",
                    value=f":globe_with_meridians: [Prendre rendez-vous]({rdv_link})",
                    inline=False
                )
            return message

    async def send(self, message):
        # Creating a webhook object
        webhook = discord.Webhook.from_url(
            self.webhook_url, session=aiohttp.ClientSession())
        # Create the payload
        await webhook.send(embed=message)


class Telegram():
    def __init__(self, api_id: int, api_hash: str, channel_id: int) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.channel_id = channel_id
        self.client = TelegramClient(
            'ants_rdv_notify', self.api_id, self.api_hash)
        self.client.start()

    def create_message(self, places):
        for place in places:
            rdv_len = len(place['available_slots'])
            print(
                f"{success()} {rdv_len} créneaux trouvé(s) à la {place['name']} !")
            print(f"{info()} Envoi de la notification sur Télégram ...")
            try:
                rdv_place_url = place['website']
                req.get(rdv_place_url)
            except Exception as e:
                print(
                    f"{warning()} Impossible de récupérer le lien du site de la {place['name']}.")
                rdv_place_url = "https://rendezvouspasseport.ants.gouv.fr"

            message = f"{rdv_len} créneaux trouvé(s) à la {place['name']}.\n"
            message += f"📍 Distance : {place['distance_km']} kms\n\n"
            for rdv in place['available_slots']:
                rdv_date = datetime.strptime(
                    rdv['datetime'], '%Y-%m-%dT%H:%M:%S+00:00')
                rdv_day = rdv_date.strftime('%d/%m/%Y')
                rdv_time = rdv_date.strftime('%H:%M')
                rdv_link = rdv['callback_url']
                message += f"📅 Le {rdv_day} à {rdv_time}\n"
                message += f"🌐 Prendre rendez-vous {rdv_link}\n"
                message += "\n"
            return message

    async def send(self, message):
        await self.client.send_message(self.channel_id, message)
