from os import path

import learn

DATA_DIR = path.join(path.dirname(path.dirname(learn.__file__)), 'data', 'images')
DESCRIPTION_FILE = path.join(DATA_DIR, "data.json")