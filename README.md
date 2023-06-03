# <img src="assets/icon.png" alt="icon" width="4%"/> Discord Calendar Bot
[![Github Version](https://img.shields.io/github/v/release/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot)
[![Github License](https://img.shields.io/github/license/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot/blob/main/LICENSE)
[![Github Last Commit](https://img.shields.io/github/last-commit/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot/commits)
[![Github Issues](https://img.shields.io/github/issues/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot/issues)

[![Python Version](https://img.shields.io/pypi/pyversions/discord-py-interactions)](https://www.python.org/downloads/)
[![Interactions.py Version](https://img.shields.io/badge/interactions.py-v5-green)](https://github.com/interactions-py/interactions.py)

[![Author](https://img.shields.io/badge/author-@LosKeeper-blue)](https://github.com/LosKeeper)
> This bot is used to display the events of the day, the next day or the week for a class. It can also display the events of a specific day and send every day a message with the events of the next day at a specific time.

## 🧾 Table of Contents
1. [🔧 Setup](#-setup)
2. [🚀 Launch](#-launch)
3. [📝 Commands](#-commands)
4. [🐞 Bugs and TODO](#-bugs-and-todo)



## 🔧 Setup
Many libraries are needed to make this bot work :
```bash
pip install -r requirements.txt
```
To configure the bot, you need to create configuration file name `.env` (you can use the `.env.example` file as a template) :
```ini
# URL of the calendar in ics format :
URL_1A=""
URL_2A_RIO=""
URL_2A_SDIA=""

# Token of the bot :
TOKEN=""

# ID of the channel where the bot will send the messages :
CHANNEL_ID_1A=""
CHANNEL_ID_2A_RIO=""
CHANNEL_ID_2A_SDIA=""

# Hour of the day when the bot will send the daily message (24h format):
HOUR=
MINUTE=
```

## 🚀 Launch
To launch the bot, you need to run the `main.py` file :
```bash
python3 main.py
```

## 📝 Commands
The bot use the slash commands to interact with the user.
| Command                      | Description                                         |
| :--------------------------- | :-------------------------------------------------- |
| `/today <classe>`            | Show the events of today for the class mentioned    |
| `/tomorrow <classe>`         | Show the events of tomorrow for the class mentioned |
| `/week <classe>`             | Show the events of the week for the class mentioned |
| `/day <YYYY-MM-DD> <classe>` | Show the events of a day for the class mentioned    |

In adition, the bot send a message at startup in the channels for each class concerning the events of the next day at the time specified in the `.env` file.

## 🐞 Bugs and TODO
- [ ] Add test for the bot
- [ ] Make code cleaner and more compact
- [ ] Add logs