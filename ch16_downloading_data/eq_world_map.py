from pathlib import Path
import json
import plotly.express as px

# Read Data as a string and convert to a Python object
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data.get("features", None)

mags, lats, longs, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lat = eq_dict["geometry"]["coordinates"][1]
    long = eq_dict["geometry"]["coordinates"][0]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    lats.append(lat)
    longs.append(long)
    eq_titles.append(eq_title)

title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats,
    lon=longs,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
