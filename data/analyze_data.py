import numpy as np
import cv2
from matplotlib import patches
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('/home/asemakov/tmp/opencv/data/haarcascade_russian_plate_number.xml')
img = cv2.imread('/home/asemakov/tmp/opencv/data/images/FILE0176.MOV.0035.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faces = face_cascade.detectMultiScale(gray, 1.3, 2)
print len(faces)
r = plt.imshow(img)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
    r.axes.add_patch(rect)
    # roi_gray = gray[y:y+h, x:x+w]
    # roi_color = img[y:y+h, x:x+w]
    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # for (ex,ey,ew,eh) in eyes:
    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


# r.figure.canvas.mpl_connect("key_press_event", handler.key_press_event)
plt.show()
