import os
import cv2
import matplotlib.pyplot as plt

#python move.py --number 2

f = open("coordinate.txt", "w")


img = cv2.imread("D:/astr/images/100.jpg")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img)
plt.show()

a = int(input("how many region wanna select?\n"))


for i in range(a):
    os.system("python click.py --number " + str(i))
