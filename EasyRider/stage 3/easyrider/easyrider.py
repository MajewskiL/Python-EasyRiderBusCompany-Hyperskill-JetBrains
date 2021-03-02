import json


def stops(json_final):
    lines = {}
    for x in json_final:
        try:
            lines[x["bus_id"]].append(x)
        except KeyError:
            lines[x["bus_id"]] = [x]
    return lines


def stage_3(json_final):
    print("Line names and number of stops:")
    lines = stops(json_final)
    for x in lines:
        print(f"bus_id: {x}, stops: {len(lines[x])}")
    pass


easy_rider = json.loads(input())
stage_3(easy_rider)
