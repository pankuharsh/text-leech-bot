import os

API_ID    = os.environ.get("API_ID", "20801703")
API_HASH  = os.environ.get("API_HASH", "08d16dc8f019dde9e43c3045cf55c019")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
