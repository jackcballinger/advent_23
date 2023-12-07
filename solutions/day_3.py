from collections import defaultdict
import re

import numpy as np

from utils import read_data


def get_touching_symbols(padded_input_data, row, start_col, offset, symbols="all"):
    sub_array = padded_input_data[
        row - 1 : row + 2, start_col - 1 : start_col + offset + 1
    ]
    if symbols == "all":
        return any(symbol in sub_array for symbol in unique_values)
    return [
        tuple(np.array(x) + np.array([row - 1, start_col - 1]))
        for x in list(zip(*np.where(sub_array == "*")))
    ]


def get_output_coords(input_padded_data, symbol):
    output_coords = []
    i, j, k = 1, 1, 0
    while True:
        cur = input_padded_data[i][j]
        if i == input_padded_data.shape[0] - 1:
            break
        if j == input_padded_data.shape[1] - 1:
            j = 1
            i += 1
        else:
            if symbol == "numbers" and re.match(r"[0-9]", cur):
                num_to_add = cur
                k = 1
                while True:
                    if re.match(r"[0-9]", input_padded_data[i][j + k]):
                        num_to_add += input_padded_data[i][j + k]
                        k += 1
                    else:
                        output_coords.append(
                            {
                                "value": num_to_add,
                                "coords": [
                                    tuple(np.array([i, j]) + np.array([0, x]))
                                    for x in range(k)
                                ],
                                "offset": k - 1,
                            }
                        )
                        j += k
                        k = 0
                        break
            elif symbol == cur == "*":
                output_coords.append({"value": "*", "coords": (i, j), "offset": 0})
                j += 1
            else:
                j += 1
    return output_coords


input_data = read_data(3, splitlines=True, splitrows=True, to_array=True)

padded_input_data = np.pad(input_data, pad_width=[(1, 1), (1, 1)], constant_values=".")

unique_values = {
    x for l in input_data for x in l if not re.match(r"[0-9]", x) and x != "."
}

# part 1

part_numbers = []
i, j, k = 1, 1, 0
while True:
    cur = padded_input_data[i][j]
    if i == padded_input_data.shape[0] - 1:
        break
    if j == padded_input_data.shape[1] - 1:
        j = 1
        i += 1
    elif re.match(r"[0-9]", cur):
        num_to_add = cur
        k = 1
        while True:
            if re.match(r"[0-9]", padded_input_data[i][j + k]):
                num_to_add += padded_input_data[i][j + k]
                k += 1
            else:
                if get_touching_symbols(padded_input_data, i, j, k):
                    part_numbers.append(int(num_to_add))
                j += k
                k = 0
                break
    else:
        j += 1

part_1 = sum(part_numbers)
# 531932


# part 2
number_coords = get_output_coords(padded_input_data, symbol="numbers")
star_coords = get_output_coords(padded_input_data, symbol="*")

gear_ratios = 0

for star_coord in star_coords:
    adjacent_coords = [
        x
        for x in [
            (star_coord["coords"][0] + i, star_coord["coords"][1] + j)
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
        ]
        if x != star_coord["coords"]
    ]
    adjacent_numbers = [
        x
        for x in number_coords
        if any(coord in adjacent_coords for coord in x["coords"])
    ]
    if len(adjacent_numbers) == 2:
        gear_ratios += np.prod([int(x["value"]) for x in adjacent_numbers])

part_2 = gear_ratios
# 73646890
