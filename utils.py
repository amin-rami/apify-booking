from typing import List


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


async def scrape(runner_per_room, template):
    pass
