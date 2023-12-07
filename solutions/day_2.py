from math import prod
import re

from utils import read_data

input_data = read_data(2, splitlines=True)


def format_row(input_row):
    return [
        {y.strip().split(" ")[1]: y.strip().split(" ")[0] for y in x.strip().split(",")}
        for x in input_row.split(";")
    ]


def parse_data(input_data):
    return {
        int(re.search(r"\d+", row).group()): format_row(row.split(":")[1])
        for row in input_data
    }


parsed_data = parse_data(input_data)

# part 1
condition = {"red": 12, "green": 13, "blue": 14}

part_1 = sum(
    [
        id
        for id, row in parsed_data.items()
        if all(
            all([int(v) <= condition[k] for k, v in cube_set.items()])
            for cube_set in row
        )
    ]
)
# 2061

# part 2
part_2 = sum(
    [
        prod([max([int(x.get(colour, 0)) for x in row]) for colour in condition.keys()])
        for row in parsed_data.values()
    ]
)
# 72596
