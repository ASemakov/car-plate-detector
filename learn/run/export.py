from learn.const import DESCRIPTION_FILE
from learn.polygon_catalog import PolygonCatalog, Polygon

catalog = PolygonCatalog.load_or_create(DESCRIPTION_FILE)


for image, polygons in catalog:
    if len(polygons) != len(set(polygons)):
        print image, len(polygons), len(set(polygons))
