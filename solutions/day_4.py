from collections import defaultdict
import re

from utils import read_data


def format_card(input_card):
    card_dict = re.search(
        r"\s+(?P<card_number>[0-9]+):\s+(?P<winning_numbers>.*)\s+\|\s+(?P<potential_numbers>.*)$",
        input_card,
    ).groupdict()
    card_dict["card_number"] = int(card_dict["card_number"])
    card_dict["winning_numbers"] = [
        int(x) for x in card_dict["winning_numbers"].split()
    ]
    card_dict["potential_numbers"] = [
        int(x) for x in card_dict["potential_numbers"].split()
    ]
    return card_dict


def format_input_data(input_data):
    return [format_card(card) for card in input_data]


input_data = read_data(4, splitlines=True)


formatted_data = format_input_data(input_data)

# part 1
part_1 = sum(
    [
        2
        ** (
            len(
                set(card["winning_numbers"]).intersection(
                    set(card["potential_numbers"])
                )
            )
            - 1
        )
        for card in formatted_data
        if (
            len(
                set(card["winning_numbers"]).intersection(
                    set(card["potential_numbers"])
                )
            )
        )
        > 0
    ]
)
# 18519

# part 2
card_nums = {card_num: 1 for card_num in range(1, len(formatted_data) + 1)}
for card in formatted_data:
    num_of_current_card = card_nums[card["card_number"]]
    cards_to_add = [
        formatted_data[card["card_number"] + x]["card_number"]
        for x in range(
            len(
                set(card["winning_numbers"]).intersection(
                    set(card["potential_numbers"])
                )
            )
        )
    ]
    for card_to_add in cards_to_add:
        card_nums[card_to_add] += 1 * num_of_current_card
part_2 = sum(card_nums.values())
# 11787590
