import re

from utils import read_data

input_data = read_data(1, splitlines=True)

mapping_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def remove_alpha_chars(input_list):
    return [re.sub(r"[a-z]+", r"", row) for row in input_list]


def convert_chars_to_ints(input_list):
    output_list = []
    for row in input_list:
        new_row = ""
        i = 0
        while i < len(row):
            cur = row[i]
            if cur in [str(x) for x in mapping_dict.values()]:
                new_row += cur
                i += 1
            elif cur in [x[0] for x in mapping_dict.keys()]:
                num_to_convert = [
                    k
                    for k in mapping_dict.keys()
                    if k.startswith(cur) and row[i : i + len(k)] == k
                ]
                if num_to_convert:
                    new_row += str(mapping_dict[num_to_convert[0]])
                    i += len(num_to_convert[0])
                else:
                    i += 1
            else:
                i += 1
        output_list.append(new_row)
    return output_list


# def format_row(input_row):
#     new_row = ""
#     i = 0
#     j = 1
#     while i + j < len(input_row) + 1:
#         cur = input_row[i : i + j]
#         if cur in [str(x) for x in list(mapping_dict.values())]:
#             new_row += str(cur)
#             i += 1
#         elif {cur}.intersection(x[:j] for x in mapping_dict.keys()):
#             if {cur}.intersection(set(mapping_dict.keys())):
#                 new_row += str(mapping_dict[cur])
#                 i += j
#                 j = 1
#             else:
#                 j += 1
#         else:
#             i += 1
#             j = 1
#     return new_row


# def convert_chars_to_ints(input_list):
#     return [format_row(row) for row in input_list]


# part 1
part_1 = sum([int(x[0] + x[-1]) for x in remove_alpha_chars(input_data)])
# 55130


# input_data = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".splitlines()

# part 2
part_2 = sum([int(x[0] + x[-1]) for x in convert_chars_to_ints(input_data)])
print("test")


# tried
# 54890 - too low
# 54978


# 54985
