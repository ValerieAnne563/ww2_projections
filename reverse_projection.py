from osgeo import ogr
from osgeo import osr


def to_projected(point, destination_zone):
	source = osr.SpatialReference()
	source.ImportFromEPSG(4326)

	target = osr.SpatialReference()
	target.ImportFromEPSG(destination_zone)

	transform = osr.CoordinateTransformation(source, target)
	point.Transform(transform)
	return(point)

# da_point_coords = ogr.CreateGeometryFromWkt("POINT (-1.40252 49.23961)")
# meters = to_projected(da_point_coords, 27571)

projected_origin = ogr.CreateGeometryFromWkt("POINT (-1.404999694339 49.175135650763)")
meters = to_projected(projected_origin, 27571)

print(meters.ExportToWkt())