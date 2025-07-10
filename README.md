# Instagram Selenium Bot

A simple Instagram bot that logs in and fetches a specified number of followers using Selenium.

## Features

- Logs into Instagram using credentials from `.env`
- Scrapes a target user's follower list
- Saves followers to `followers.txt`

## Usage

1. Create a `.env` file with your Instagram credentials:

```
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

2. Install dependencies:

```
pip install selenium python-dotenv
```

3. Run the bot:

```
python instagram_bot.py
```

## Disclaimer

This bot is for educational purposes only.
