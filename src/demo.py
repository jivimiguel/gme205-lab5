from shapely.geometry import Polygon, LineString
from spatial import Parcel, Building, Road

parcel = Parcel(Polygon([(0,0),(1,0),(1,5),(0,5)]))
building = Building(Polygon([(0,0),(10,0),(10,10),(0,10)]), 3)
road = Road(LineString([(0,0),(5,0)]), 2)

features = [parcel, building, road]

for f in features:
    print(type(f).__name__, f.effective_area())