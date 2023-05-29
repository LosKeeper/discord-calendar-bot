# <img src="assets/icon.png" alt="icon" width="4%"/> Discord Calendar Bot
[![Github Version](https://img.shields.io/github/v/release/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot)
[![Github License](https://img.shields.io/github/license/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot/blob/main/LICENSE)
[![Github Last Commit](https://img.shields.io/github/last-commit/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot/commits)
[![Github Issues](https://img.shields.io/github/issues/loskeeper/discord-calendar-bot)](https://github.com/LosKeeper/discord-calendar-bot/issues)

[![Python Version](https://img.shields.io/pypi/pyversions/discord-py-interactions)](https://www.python.org/downloads/)
[![Interactions.py Version](https://img.shields.io/badge/interactions.py-v5-green)](https://github.com/interactions-py/interactions.py)

[![Author](https://img.shields.io/badge/author-@LosKeeper-blue)](https://github.com/LosKeeper)
> This bot is used to display the events of the day, the next day or the week for a class. It can also display the events of a specific day.

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
To configure the bot, you need to create configuration file name `config.py` : 
```python
# URL of the calendar in ics format :
url_1a = ""
url_2a_rio = ""
url_2a_sdia = ""

# Token of the bot :
token = ""

# ID of the channel where the bot will send the messages :
CHANNEL_ID_1A = ""
CHANNEL_ID_2A_RIO = ""
CHANNEL_ID_2A_SDIA = ""
```

## 🚀 Launch
To launch the bot, you need to run the `calendar-bot.py` file :
```bash
python3 calendar-bot.py
```

## 📝 Commands
The bot use the slash commands to interact with the user.
| Command                      | Description                                         |
| :--------------------------- | :-------------------------------------------------- |
| `/today <classe>`            | Show the events of today for the class mentioned    |
| `/tomorrow <classe>`         | Show the events of tomorrow for the class mentioned |
| `/week <classe>`             | Show the events of the week for the class mentioned |
| `/day <YYYY-MM-DD> <classe>` | Show the events of a day for the class mentioned    |

In adition, the bot send a message at startup in the channels for each class concerning the events of the next day.

## 🐞 Bugs and TODO
- [ ] Create auto post every morning using something else than restart the bot with cron
- [x] Migration to interactions.py v5
- [ ] Use time from the computer instead of UTC time
- [ ] Use .env file for token and channel id instead of config.py
