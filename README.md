# Discord Calendar Bot
> The bot is currently in development.

> Many libraries are needed to make this bot work.
```pwsh
pip install -r requirements.txt
```


## Configuration
To configure the bot, you need to create a configuration file call `config.py`.
```python
url = # URL of the calendar in ics format 
token = # Token of the bot 
```

## Functions
The bot use the slash commands to interact with the user.
| Command             | Description                 |
| :------------------ | :-------------------------- |
| `/help`             | Show the help message       |
| `/today`            | Show the events of today    |
| `/tomorrow`         | Show the events of tomorrow |
| `/week`             | Show the events of the week |
| `/day <YYYY-MM-DD>` (Not currently working) | Show the events of a day    |

## TODO
- Create help command
- Create day command with slash interactions
