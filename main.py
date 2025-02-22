from dotenv import load_dotenv
from utils import create_run_inputs, scrape
import os
from apify_client import ApifyClientAsync
import json
import asyncio


load_dotenv()


API_TOKEN = os.getenv("APIFY_API_TOKEN")
ACTOR_ID = os.getenv("ACTOR_ID")
MIN_PRICE = int(os.getenv("MIN_PRICE"))
MAX_PRICE = int(os.getenv("MAX_PRICE"))
runners_per_room = json.loads(os.getenv("RUNNERS_PER_ROOM"))


client = ApifyClientAsync(API_TOKEN)
template = {
        "adults": None,
        "rooms": None,
        "minMaxPrice": None,
        "checkIn": os.getenv("CHECK_IN"),
        "checkOut": os.getenv("CHECK_OUT"),
        "currency": "USD",
        "language": "en-gb",
        "maxItems": 100000,
        "propertyType": "none",
        "search": "Dubai",
        "starsCountFilter": "any"
    }
run_inputs = create_run_inputs(runners_per_room, (MIN_PRICE, MAX_PRICE), template)
asyncio.run(scrape(client, ACTOR_ID, run_inputs))
