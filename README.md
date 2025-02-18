
<div align="center">

<!--  <img src="assets/logo.png" alt="logo" width="200" height="auto" />-->
  <h1>A French NIC and Passport rendez-vous notifier</h1>
  
  <p>
    A python tool to get notified for French NIC and Passport rendez-vous from the <a href="https://rendezvouspasseport.ants.gouv.fr">ANTS service</a> !
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://www.python.org/downloads/release/python-3132/">
    <img src="https://img.shields.io/badge/python-3.13.2-blue.svg">
  </a>
  <a href="https://github.com/0xsysr3ll/ants-rdv-notify/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/0xsysr3ll/ants-rdv-notify" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/0xsysr3ll/ants-rdv-notify" alt="last update" />
  </a>
  <a href="https://github.com/0xsysr3ll/ants-rdv-notify/network/members">
    <img src="https://img.shields.io/github/forks/0xsysr3ll/ants-rdv-notify" alt="forks" />
  </a>
  <a href="https://github.com/0xsysr3ll/ants-rdv-notify/stargazers">
    <img src="https://img.shields.io/github/stars/0xsysr3ll/ants-rdv-notify" alt="stars" />
  </a>
  <a href="https://github.com/0xsysr3ll/ants-rdv-notify/issues/">
    <img src="https://img.shields.io/github/issues/0xsysr3ll/ants-rdv-notify" alt="open issues" />
  </a>
  <a href="https://hub.docker.com/r/0xsysr3ll/ants-rdv-notify">
    <img src="https://img.shields.io/docker/pulls/0xsysr3ll/ants-rdv-notify" alt="docker pulls" />
  </a>
</p>
 
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
- [Usage](#eyes-usage)
- [Contributing](#wave-contributing)
- [Contact](#handshake-contact)

  

<!-- About the Project -->
## :star2: About the Project

This Python script periodically searches for available rendez-vous slots for French national identity cards (CNI) and passports at https://rendezvouspasseport.ants.gouv.fr using the API provided by the French government. When a slot is found, it sends a notification to a Discord webhook.

<!-- Getting Started -->
## :toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

To run this script, you will need :
- python 3 or Docker (recommended)
- A discord webhook : see the [official documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)


<!-- Installation -->
### :gear: Installation

#### Local
1. Clone this repository:
    ```bash
    git clone https://github.com/0xSysR3ll/ants-rdv-notify
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Copy the `config/config-sample.yml` to `app/config/config.yml` and edit the values to match your preferences.

4. Run the script:
    ```bash
    python3 main.py
    ```

#### Docker

1. Clone this repository:
    ```bash
    git clone https://github.com/0xSysR3ll/ants-rdv-notify
    ```

2. Copy the `config/config-sample.yml` to `config/config.yml` and edit the values to match your preferences.

3. Pull the official image on Docker Hub
    ```bash
    docker pull ghcr.io/0xsysr3ll/ants-rdv-notify:latest
    ```

4. Copy `docker-compose.sample.yml` to `docker-compose.yml` and adapt it to your needs.

5. Start the docker
    ```bash
    docker compose up -d
    ```

#### Configuration

Configuration File (config.yml) Documentation

##### General Settings

The `config.yml` file is used to configure various settings for an application. It contains the following settings:
General Settings

- `city`: Specifies the city for which the application will retrieve information. The format is as follows: city: # City Name PostalCode. For example, city: # Paris 75000.

- `reason`: Specifies the reason for document retrieval. It can be one of the following options: CNI (National Identity Card), PASSPORT, or CNI-PASSPORT (for both). For example, reason: # CNI, PASSPORT, CNI-PASSPORT (for both).

- `documents_number`: Specifies the number of documents to be retrieved. It should be a value between 1 and 5. For example, documents_number: # From 1 to 5.

- `radius_km`: Specifies the radius in kilometers within which the application will search for document retrieval. It can be one of the following options: 20, 30, or 60. For example, `radius_km`: # 20, 30, 60 (kms).

##### Notifiers Settings

The notifiers section allows you to configure different notification systems. Currently, the following notifiers are supported:
Discord Notifier

To enable Discord notifications, uncomment the following lines:
```yml
discord:
  webhook_url:
```

- `webhook_url`: Specifies the Discord webhook URL to which the application will send notifications. You can obtain the webhook URL by following the instructions provided in the Discord Webhooks documentation.

##### Telegram Notifier

To enable Telegram notifications, uncomment the following lines:

```yml
telegram:
    api_id:
    api_hash:
    channel_id:
```

- `api_id`: Specifies the API ID for your Telegram application. You can obtain this value by creating a new application on the Telegram API development platform and retrieving the API ID.

- `api_hash`: Specifies the API hash for your Telegram application. You can obtain this value from the same page where you retrieved the API ID.

- `channel_id`: Specifies the ID of the Telegram channel where the notifications will be sent. You need to create a Telegram channel and obtain the channel ID.

Note: Make sure to uncomment the necessary lines and provide the required values for the chosen notification systems.

<!-- Contributing -->
## :wave: Contributing

Contributions are always welcome, I am not a pro developer !

<!-- Contact -->
## :handshake: Contact

0xSysr3ll - [@0xsysr3ll](https://twitter.com/0xsysr3ll) - 0xsysr3ll@pm.me
