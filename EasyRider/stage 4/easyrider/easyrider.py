import json


def stage_4(json_final):
    all_stops = {}
    for z in set([x["bus_id"] for x in json_final]):
        all_stops[z] = [x for x in json_final if x["bus_id"] == z]
    station_s, station_f, station_o = [], [], []
    for x in all_stops:
        z = "".join([y["stop_type"] for y in all_stops[x]])
        if any(["S" not in z, "F" not in z]):
            print(f"There is no start or end stop for the line: {all_stops[x][0]['bus_id']}.")
            return
        for y in all_stops[x]:
            if y["stop_type"] == "S":
                station_s.append(y["stop_name"])
            if y["stop_type"] == "F":
                station_f.append(y["stop_name"])
            station_o.append(y["stop_name"])
    print(f"Start stops: {len(set(station_s))} {sorted(set(station_s))}")
    print(f"Transfer stops: {len([x for x in set(station_o) if station_o.count(x) > 1])} {sorted([x for x in set(station_o) if station_o.count(x) > 1])}")
    print(f"Finish stops: {len(set(station_f))} {sorted(set(station_f))}")


easy_rider = json.loads(input())
stage_4(easy_rider)

'''

import json
import itertools


def stops(json_final):
    lines = {}
    for x in json_final:
        try:
            lines[x["bus_id"]].append(x)
        except KeyError:
            lines[x["bus_id"]] = [x]
    return lines


def lines(stops_table):
    all_stops, stops_tmp, station_s, station_f = [], [], [], []
    names = {}
    for x in stops_table:
        for y in stops_table[x]:
            stops_tmp.append(y["stop_id"])
            if y["stop_type"] == "S":
                station_s.append(y["stop_id"])
            elif y["stop_type"] == "F":
                station_f.append(y["stop_id"])
            names[y["stop_id"]] = y["stop_name"]
        all_stops.append(set(stops_tmp))
        stops_tmp = []

    stop_type = []
    for z in itertools.combinations(range(len(all_stops)), 2):
        stop_type.append((all_stops[z[0]].intersection(all_stops[z[1]])))

    station_o = set()
    for z in stop_type:
        station_o = station_o | z
    dane = dict()
    dane["names"] = names
    dane["station_o"] = set(station_o)
    dane["station_s"] = set(station_s)
    dane["station_f"] = set(station_f)
    return dane


def stage_4(json_final):
    all_stops = stops(json_final)
    print(all_stops)
    data = lines(all_stops)
    for x in all_stops:
        if ("S" or "F") not in "".join([y["stop_type"] for y in all_stops[x]]):
            print(f"There is no start or end stop for the line: {all_stops[x][0]['bus_id']}.")
            return
    if not data:
        return
    names = data["names"]
    station_s_n = [names[x] for x in set(data["station_s"])]
    station_f_n = [names[x] for x in set(data["station_f"])]
    station_s_o = [names[x] for x in data["station_o"]]
    print(f"Start stops: {len(station_s_n)} {sorted(station_s_n)}")
    print(f"Transfer stops: {len(station_s_o)} {sorted(station_s_o)}")
    print(f"Finish stops: {len(station_f_n)} {sorted(station_f_n)}")


easy_rider = json.loads('[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, '
                           '{"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, '
                           '{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, '
                           '{"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, '
                           '{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "", "a_time" : "08:13"}, '
                           '{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]')
easy_rider = json.loads(input())

stage_4(easy_rider)
'''
