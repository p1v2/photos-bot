import os

# Token to auth for the telegram API
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
# Fallback search word
FALLBACK_TEXT = "sunset"

# Giphy API key to auth to giphy
GIPHY_KEY = os.environ.get("GIPHY_KEY")
