from pathlib import Path
import json

# Read Data as a string and convert to a Python object
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data.get("features", None)
print(len(all_eq_dicts))

mags, lats, longs = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lat = eq_dict["geometry"]["coordinates"][1]
    long = eq_dict["geometry"]["coordinates"][0]
    mags.append(mag)
    lats.append(lat)
    longs.append(long)

print(mags[:10])
print(lats[:10])
print(longs[:10])
