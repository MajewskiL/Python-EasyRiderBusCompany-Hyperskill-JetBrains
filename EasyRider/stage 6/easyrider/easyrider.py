import json

def stage_6(json_final):
    print("On demand stops test:")
    all_stops = {}
    for z in set([x["bus_id"] for x in json_final]):
        all_stops[z] = [x for x in json_final if x["bus_id"] == z]
    station_all = [x["stop_name"] for y in all_stops for x in all_stops[y]]
    station_sf = [x["stop_name"] for y in all_stops for x in all_stops[y] if x["stop_type"] in ("SF") and x["stop_type"] != ""]
    station_o = [x["stop_name"] for y in all_stops for x in all_stops[y] if x["stop_type"] in ("O") and x["stop_type"] != ""]
    station_t = sorted([x for x in set(station_all) if station_all.count(x) > 1])
    stations = (set(station_sf) | set(station_t)) & set(station_o)
    if stations:
        print(f"Wrong stop type: {sorted(stations)}")
    else:
        print("OK")


easy_rider = json.loads(input())
stage_6(easy_rider)
