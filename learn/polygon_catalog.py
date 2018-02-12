class Polygon(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return "Polygon({},{},{},{})".format(self.x, self.y, self.w, self.h)

    def __repr__(self):
        return str(self)


class PolygonCatalog(object):
    def __init__(self):
        self._catalog = {}

    def add_polygon(self, image_name, polygon):
        self._catalog.setdefault(image_name, []).append(polygon)

    def remove_image(self, image_name):
        self._catalog.pop(image_name, None)

    def get_for_image(self, image):
        return self._catalog.get(image, [])

    def __str__(self):
        return str(self._catalog)

    def __repr__(self):
        repr(self._catalog)
