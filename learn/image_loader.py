import os


class ImageLoader(object):
    def __init__(self, directory):
        self._dir = directory
        self.files = list(self._load_files())

    def _load_files(self):
        for dirName, subdirList, fileList in os.walk(self._dir):
            for fname in fileList:
                if fname.endswith(".jpg"):
                    yield os.path.join(dirName, fname)

    def __getitem__(self, item):
        return self.files[item]

    def __len__(self):
        return len(self.files)