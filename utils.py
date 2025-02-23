from typing import List, Iterable
from apify_client import ApifyClientAsync
import asyncio


def create_run_inputs(runners_per_room: dict, minMaxPrice: tuple, template: dict) -> List[dict]:
    min_price, max_price = minMaxPrice
    run_inputs = []

    for rooms, runners in runners_per_room.items():
        rooms, runners = int(rooms), int(runners)
        increment = (max_price - min_price) // runners

        for i in range(runners):
            start = min_price + i * increment
            end = max_price if i == runners - 1 else min_price + (i + 1) * increment

            run_input = dict(template)
            run_input["adults"] = rooms
            run_input["rooms"] = rooms
            run_input["minMaxPrice"] = f"{start}-{end}"
            run_inputs.append(run_input)
    return run_inputs


def create_chunks(iterable: Iterable, chunk_size: int):
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i: i + chunk_size]


async def scrape(client: ApifyClientAsync, actor_id: str, run_inputs: List[dict]):
    tasks = [client.actor(actor_id).start(run_input=run_input, timeout_secs=36000) for run_input in run_inputs]
    await asyncio.gather(*tasks)


async def push_data_to_target_dataset(
    client: ApifyClientAsync,
    origin_dataset_id: str,
    destination_dataset_id: str,
    chunk_size: int
) -> None:
    data = await client.dataset(origin_dataset_id).list_items()
    data = data.items
    chunks = create_chunks(data, chunk_size)
    for chunk in chunks:
        await client.dataset(destination_dataset_id).push_items(chunk)
