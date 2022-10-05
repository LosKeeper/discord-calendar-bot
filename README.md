# Discord Calendar Bot
> The bot is currently in development.
> THE BOT USE UTC TIMEZONE !!!

> Many libraries are needed to make this bot work.
```pwsh
pip install -r requirements.txt
```


## Configuration
To configure the bot, you need to create configuration file name `config.py`.
```python
# URL of the calendar in ics format :
url_1a = 
url_2a_rio = 
url_2a_sdia = 

# Token of the bot :
token = 

# ID of the channel where the bot will send the messages :
CHANNEL_ID_1A = 
CHANNEL_ID_2A_RIO = 
CHANNEL_ID_2A_SDIA = 
```

## Functions
The bot use the slash commands to interact with the user.
| Command                      | Description                                             |
| :--------------------------- | :------------------------------------------------------ |
| `/today <classe>`            | Show the events of today for the class mentioned        |
| `/tomorrow <classe>`         | Show the events of tomorrow for the class mentioned     |
| ~~`/week <classe>`~~         | ~~Show the events of the week for the class mentioned~~ |
| `/day <YYYY-MM-DD> <classe>` | Show the events of a day for the class mentioned        |

In adition, the bot send a message at startup in the channels for each class concerning the events of the next day.

## TODO
- [ ] Correct the command to show the events of the week
- [ ] Create auto post every morning using something else than restart the bot with cron
- [x] Add room to the events
