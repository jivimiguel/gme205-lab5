import json
from shapely.geometry import shape
from spatial import Parcel, Building, Road

with open("data/spatial_features.json") as f:
    data = json.load(f)

features = []

for item in data:
    geom = shape(item["geometry"])
    ftype = item["type"]
    
    if ftype == "Parcel":
        obj = Parcel(geom)
        
    elif ftype == "Building":
        obj = Building(geom, item["floors"])
        
    elif ftype == "Road":
        obj = Road(geom, item["width"])
        
    features.append(obj)
    
if not features:
    print("No features found!")
    exit()
    
total_area = 0
for f in features:
    total_area += f.effective_area()

print ("Total area: ", total_area)