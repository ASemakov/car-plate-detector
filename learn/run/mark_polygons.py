from __future__ import print_function
import cv2
from matplotlib import patches
from matplotlib import pyplot as plt

from learn.image_loader import ImageLoader
from learn.polygon_catalog import PolygonCatalog, Polygon

figure = plt.figure(1)

class EventHandler(object):
    def __init__(self, image_loader, polygon_manager):
        """
        :param ImageLoader image_loader:
        :param PolygonCatalog polygon_manager:
        """
        super(EventHandler, self).__init__()
        self.x = None
        self.y = None
        self.image_loader = image_loader
        self.polygon_manager = polygon_manager
        self.image_index = 0
        self.show_image()

    def button_press_event(self, event):
        """
        :param matplotlib.backend_bases.MouseEvent event:
        """
        print("press", event.x, event.y)
        self.x = event.xdata
        self.y = event.ydata

    def button_release_event(self, event):
        """
        :param matplotlib.backend_bases.MouseEvent event:
        """
        print("release", event.x, event.y)
        self.x = self.y = None

    def motion_notify_event(self, event):
        """
        :param matplotlib.backend_bases.MouseEvent event:
        """
        if self.x is None or self.y is None:
            return
        rect = patches.Rectangle((self.x, self.y), event.xdata - self.x, event.ydata - self.y, linewidth=1, edgecolor='r', facecolor='none')
        while len(figure.gca().patches) > len(self.polygon_manager.get_for_image(self.image_loader[self.image_index])):
            figure.gca().patches.pop()
        figure.gca().add_patch(rect)
        figure.canvas.draw()

    def key_press_event(self, event):
        """
        :param matplotlib.backend_bases.KeyEvent event:
        """
        if event.key == "escape":
            while len(figure.gca().patches) > len(self.polygon_manager.get_for_image(self.image_loader[self.image_index])):
                figure.gca().patches.pop()
            figure.canvas.draw()
        if event.key == "enter" and figure.gca().patches:
            rectangle = figure.gca().patches[0]
            """:type: patches.Rectangle"""
            image_name = self.image_loader[self.image_index]
            self.polygon_manager.remove_image(image_name)
            x, y = rectangle.xy
            self.polygon_manager.add_polygon(image_name, Polygon(x, y, rectangle.get_width(), rectangle.get_height()))
        if event.key == "right":  # Next image
            self.image_index = min(len(self.image_loader) - 1, self.image_index + 1)
            self.show_image()  # Previous image
        if event.key == "left":
            self.image_index = max(0, self.image_index - 1)
            self.show_image()

    def show_image(self):
        del figure.gca().patches[:]
        image_name = self.image_loader[self.image_index]
        img = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)
        r = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        figure.gca().imshow(r)
        for p in self.polygon_manager.get_for_image(image_name):
            assert isinstance(p, Polygon)
            rect = patches.Rectangle((p.x, p.y), p.w, p.h, linewidth=1, edgecolor='r', facecolor='none')
            figure.gca().add_patch(rect)

handler = EventHandler(ImageLoader("/home/asemakov/tmp/opencv/data/images"), PolygonCatalog())
figure.canvas.mpl_connect("button_press_event", handler.button_press_event)
figure.canvas.mpl_connect("button_release_event", handler.button_release_event)
figure.canvas.mpl_connect("motion_notify_event", handler.motion_notify_event)
figure.canvas.mpl_connect("key_press_event", handler.key_press_event)

plt.show()
