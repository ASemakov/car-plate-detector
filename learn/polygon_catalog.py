import jsonpickle
from os import path


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

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y and self.w == other.h and self.y == other.h

    def __cmp__(self, other):
        return (self.x - other.x) * 10**5 + self.y - other.y

    def __hash__(self):
        return self.x*10**9 + self.y*10**6 + self.h*10**3 + self.w

class PolygonCatalog(object):
    def __init__(self, data_file):
        self._catalog = {}
        self._data_file = data_file

    def __iter__(self):
        return iter(self._catalog.items())

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

    def save(self):
        with open(self._data_file, 'w') as f:
            f.write(jsonpickle.dumps(self))
        print "Saved {0}".format(self._data_file)

    @classmethod
    def load_or_create(cls, data_file):
        try:
            with open(data_file, "r") as f:
                data = jsonpickle.loads(f.read())
            print "Loaded {0}".format(data_file)
        except:
            data = cls(data_file)
            print("Can't load {0}".format(data_file))
        return data

