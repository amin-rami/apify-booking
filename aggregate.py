import json
import os
from dotenv import load_dotenv
from apify_client import ApifyClientAsync
from utils import push_data_to_target_dataset
import asyncio
from tqdm import tqdm

load_dotenv()


API_TOKEN = os.getenv("APIFY_API_TOKEN")
client = ApifyClientAsync(API_TOKEN)


config_file_path = "dataset_config.json"
with open(config_file_path) as file:
    config = json.load(file)

origin_ids = config["origin_ids"]
destination_id = config["destination_id"]
chunk_size = 150


async def push():
    for origin_id in tqdm(origin_ids):
        await push_data_to_target_dataset(client, origin_id, destination_id, chunk_size)

asyncio.run(push())
