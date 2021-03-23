import json
import re


def stage_2(json_final):
    stop_name, stop_type, a_time = 0, 0, 0
    for x in json_final:
        if not re.match(r'^[A-Z].* Street$|^[A-Z].* Avenue$|^[A-Z].* Boulevard$|^[A-Z].* Road$', x["stop_name"]):
            #print(x["stop_name"])
            stop_name += 1
        if len(x["stop_type"]) != 0 and not re.match(r'^[SOF]$', x["stop_type"]):
            stop_type += 1
        if not re.match(r'^[0-2][0-9]:[0-5][0-9]$', x["a_time"]):
            a_time += 1
    print(f"Format validation: {stop_name + stop_type + a_time} errors")
    print(f"stop_name: {stop_name}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")


easy_rider = json.loads(input())
stage_2(easy_rider)
