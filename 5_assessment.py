import cv2
import numpy as np

xi, yi = -1, -1

drawing = False


def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), 3)


cv2.namedWindow(winname="my_image")

cv2.setMouseCallback("my_image", draw_circle)

img = cv2.imread("DATA/dog_backpack.jpg")

while True:
    cv2.imshow("my_image", img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
