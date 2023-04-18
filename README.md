
<div align="center">

<!--  <img src="assets/logo.png" alt="logo" width="200" height="auto" />-->
  <h1>A French NIC and Passport rendez-vous notifier</h1>
  
  <p>
    A python tool to get notified for French NIC and Passport rendez-vous from the <a href="https://rendezvouspasseport.ants.gouv.fr">ANTS service</a> !
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://www.python.org/downloads/release/python-3108/">
    <img src="https://img.shields.io/badge/python-3.10.8-blue.svg">
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

3. Copy the `config.yml` to the app folder and edit the values to match your preferences.

4. Run the script:
    ```bash
    python3 main.py
    ```

#### Docker

1. Clone this repository:
    ```bash
    git clone https://github.com/0xSysR3ll/ants-rdv-notify
    ```

2. Edit the values in `config.yml` to match your preferences.

3. Pull the official image on Docker Hub
    ```bash
    docker pull registry.0xsysr3ll.fr/ants-rdv-notify:latest
    ```
4. Start the docker
    ```bash
    docker compose up -d
    ```

#### Configuration

The `config.json` file contains the following settings:

- `city`: The name of the city where you want to search for rendez-vous slots.
- `reason`: The type of document you want. Options are : CNI, PASSPORT or CNI-PASSPORT (for both).
- `documents_number`: The number of people wishing for a rendez-vous.
- `radius_km`: The radius in kilometers around the city where you want to search for rendez-vous slots.
- `webhook_url`: The URL of the Discord webhook to which notifications will be sent.

<!-- Contributing -->
## :wave: Contributing

Contributions are always welcome, I am not a pro developer !

<!-- Contact -->
## :handshake: Contact

0xSysr3ll - [@0xsysr3ll](https://twitter.com/0xsysr3ll) - 0xsysr3ll@pm.me
