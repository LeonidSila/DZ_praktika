import os
import json

from itertools import zip_longest


def groping(
        output_pth="./out.txt",
        user_pth="./users.csv",
        hobby_pth="./hobby.csv"):
    if not (os.path.isfile(user_pth) or
            os.path.isfile(hobby_pth)):
        return -1
    user_lines = None
    hobby_lines = None
    with open(user_pth, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()
    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()
    if len(user_lines) < len(hobby_lines):
        return 1
    group = {}
    for fio, hobby in zip_longest(user_lines, hobby_lines):
        fio = fio.replace("\n", "")
        group[fio] = hobby.replace("\n", "") if hobby else None
    with open(output_pth, "w+", encoding="utf-8") as out_file:
        json.dump(group, out_file)
        out_file.writelines(json.dumps(group))
    return 0
if __name__ == "__main__":
    exit(groping())