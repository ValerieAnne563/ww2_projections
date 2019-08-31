from osgeo import ogr
from osgeo import osr

import numpy as np

def to_meters(str):
	vt_zone_offset = np.array([300000.0, 1000000.0])
	easting = int(str[2:5]) * 100
	northing = int(str[5:9]) * 100

	return vt_zone_offset + np.array([easting, northing])

source = osr.SpatialReference()
source.ImportFromEPSG(27571)

target = osr.SpatialReference()
target.ImportFromEPSG(4326)

transform = osr.CoordinateTransformation(source, target)

e, n = to_meters("vt278778") #fr lz 1

point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(e, n)
# point = ogr.CreateGeometryFromWkt("POINT (300000 1000000)")
point.Transform(transform)

# go_back = osr.CoordinateTransformation(target, source)
# # point = ogr.CreateGeometryFromWkt("POINT (-1.41149, 49.26723)")
# point = ogr.CreateGeometryFromWkt("POINT (-1.40252 49.23961)")
# point.Transform(go_back)

print ("%d, %d" % (point.GetY(), point.GetX()))
print (point.ExportToWkt())


