import sys
import json

def item_to_string(obj):
    return '\t'.join(str(v) for v in [
        obj["id"],
        0,
        obj["frame"],
        obj["command"],
        obj["param1"],
        obj["param2"],
        obj["param3"],
        obj["param4"],
        obj["coordinate"][0],
        obj["coordinate"][1],
        obj["coordinate"][2],
        1 if obj["autoContinue"] else 0
    ]) + "\r\n"

args = sys.argv[1:]

if not args:
    print("Please provide the path to a `.mission` (json) file from QGroundCommand")
    sys.exit(1)

mission_path = args[0]

json_data = {}
with open(mission_path) as data_file:
    json_data = json.load(data_file)

if not json_data["plannedHomePosition"]:
    print("No planned home position set!")
    sys.exit(2)

home = json_data["plannedHomePosition"]
output_str = "QGC WPL 110\r\n" + item_to_string(home)

for item in json_data["items"]:
    output_str += item_to_string(item)

print(output_str)