import cv2
import numpy as np

# VARIABLES
drawing = False  # True while mouse down, False when mouse is up
ix, iy = -1, -1


# FUNCTION
def draw_rectangle(event, x, y, flags, params):
    # Grab the global variables
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 225, 0), -1)


# SHOWING THE IMAGE

# Black image
img = np.zeros((512, 512, 3))

# Connect is with a name window
cv2.namedWindow(winname="my_drawing")

cv2.setMouseCallback("my_drawing", draw_rectangle)

while True:
    cv2.imshow("my_drawing", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
