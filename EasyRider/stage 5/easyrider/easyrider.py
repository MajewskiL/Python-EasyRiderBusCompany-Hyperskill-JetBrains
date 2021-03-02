import json


def stops(json_final):
    lines = {}
    for x in json_final:
        try:
            lines[x["bus_id"]].append(x)
        except KeyError:
            lines[x["bus_id"]] = [x]
    return lines


def stage_5(json_final):
    print("Arrival time test:")
    error = 0
    stops_all = stops(json_final)
    for x in stops_all:
        times, start = {}, ""
        for y in stops_all[x]:
            if y["stop_type"] == "S":
                start = str(y["stop_id"])
            times[str(y["stop_id"])] = (str(y["next_stop"]), y["a_time"], y["stop_name"])
        e, t, n = times[start]
        while e != "0":
            if t >= times[e][1]:
                print(f"bus_id line {x}: wrong time on station {times[e][2]}")
                error += 1
                break
            e, t, n = times[e]
    if error == 0:
        print("OK")


easy_rider = json.loads(input())
stage_5(easy_rider)
