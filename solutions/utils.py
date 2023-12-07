from pathlib import Path

import numpy as np


def read_data(input_day, splitlines=False, splitrows=False, to_array=False):
    with open(
        Path(__file__).parent.parent / "inputs" / f"day_{input_day}.txt", "r"
    ) as f:
        input_data = f.read()
    if splitlines:
        input_data = input_data.splitlines()
    if splitrows:
        input_data = [[y for y in x] for x in input_data]
    if to_array:
        input_data = np.array(input_data)
    return input_data
