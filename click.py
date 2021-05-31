import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.widgets import Cursor
import argparse


img = cv2.imread("D:/astr/images/100.jpg")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img)



parser = argparse.ArgumentParser()
parser.add_argument("--number", help="number of region", type = int )
args = vars(parser.parse_args())

m = args['number']
print(m)


box_x = []
box_y = []

def onclick(event):
    print(event.xdata)
    print(event.ydata)
    print()
    box_x.append(event.xdata)
    box_y.append(event.ydata)
    if len(box_x) == 4:
        fig.canvas.mpl_disconnect(cid)
        plt.close()


cid = fig.canvas.mpl_connect('button_press_event', onclick)


cursor = Cursor(ax, color = 'g', linewidth = 2)
# Bring up the figure (and wait)
plt.show()


box_x = sorted(box_x)
box_y = sorted(box_y)

crop_img = img[int(box_y[0]):int(box_y[3]), int(box_x[0]):int(box_x[3])]
#plt.imshow(crop_img)

#img_name = "cropped"+str(m)
plt.imsave("cropped"+str(m) +".jpg", crop_img)
plt.imshow(crop_img)
plt.show()
f = open("coordinate.txt", "a")
txt = str(box_x[0]) + ", "+ str(box_y[0]) + ", "+ str(box_x[3]) + ", "+ str(box_y[3]) + "\n"
f.write(txt)
f.close()
