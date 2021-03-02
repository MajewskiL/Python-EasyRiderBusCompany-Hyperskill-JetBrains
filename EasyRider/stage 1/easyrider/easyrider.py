import json


def stage_1(json_final):
    bus_id, stop_id, stop_name, next_stop, stop_type, a_time = 0, 0, 0, 0, 0, 0
    for x in json_final:
        if not isinstance(x["bus_id"], int):
            bus_id += 1
        if not isinstance(x["stop_id"], int):
            stop_id += 1
        if not isinstance(x["stop_name"], str) or x["stop_name"] == "":
            stop_name += 1
        if not isinstance(x["next_stop"], int) or x["next_stop"] == "":
            next_stop += 1
        if not isinstance(x["stop_type"], str) or len(x["stop_type"]) > 1:
            stop_type += 1
        if not isinstance(x["a_time"], str) or x["a_time"] == "":
            a_time += 1
    print(f"{bus_id + stop_id + stop_name + next_stop + stop_type + a_time} errors")
    print(f"bus_id: {bus_id}")
    print(f"stop_id: {stop_id}")
    print(f"stop_name: {stop_name}")
    print(f"next_stop: {next_stop}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")

easy_rider = json.loads(input())
stage_1(easy_rider)
