from typing import List


def create_run_inputs_from_room_config(runner_per_room: dict, template: dict) -> List[dict]:
    min_price, max_price = template["minMaxPrice"].split("-")
    min_price, max_price = int(min_price), int(max_price)

    run_inputs = []

    for rooms, runners in template["rooms"].items():
        increment = (max_price - min_price) // runners

        for i in range(runners):
            start = min_price + i * increment
            end = max_price if i == runners - 1 else min_price + (i + 1) * increment

            run_input = dict(template)
            run_input["adults"] = rooms
            run_input["rooms"] = rooms
            run_input["minMaxPrice"] = f"{start}-{end}"
            run_inputs.append(run_input)


async def scrape(runner_per_room, template):
    pass
