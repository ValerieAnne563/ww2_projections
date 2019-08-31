from osgeo import ogr
from osgeo import osr

import numpy as np

flz1_projected_origin = 40063.0848, 1067022.9279
vt_zone_offset = np.array([300000.0, 1000000.0])
vx_zone_offset = np.array([200000.0, 0])
vV_zone_offset = np.array([0.0, 0])

offsets = {"vt": vt_zone_offset,
           "vV": vV_zone_offset,
           "VX": vx_zone_offset}

def get_tile_offset(tile):
	
	offset =  offsets[tile]
	if(offset is not None):
		return(offset)
	else:
		raise ("Unknown offset for tile %s" % tile)

def to_meters(projection_origin, coordinates_str):
	
	tile_offset = get_tile_offset(coordinates_str[0:2])
	easting = int(coordinates_str[2:5]) * 100
	northing = int(coordinates_str[5:9]) * 100

	return projection_origin + tile_offset + np.array([easting, northing])

def towgs84(point, source_zone):
	source = osr.SpatialReference()
	source.ImportFromEPSG(source_zone)

	target = osr.SpatialReference()
	target.ImportFromEPSG(4326)

	transform = osr.CoordinateTransformation(source, target)
	point.Transform(transform)

	return(point)

def decode_flz1(coordinates_str):
	zone_origin = flz1_projected_origin
	epsg_code = 27571

	e, n = to_meters(zone_origin, coordinates_str)
	print([e, n])

	point = ogr.Geometry(ogr.wkbPoint)
	point.AddPoint(e, n)

	return towgs84(point, epsg_code)

# projected_point = decode_flz1("vt278778")	
# actual = np.array([49.23961, -1.40252])

# print(projected_point.ExportToWkt())
# print(actual)


# demo_point = decode_flz1("VX962494")
# print(demo_point.ExportToWkt())

zero_point = decode_flz1("vV000000")	
print(zero_point.ExportToWkt())






# point = ogr.CreateGeometryFromWkt("POINT (300000 1000000)")




