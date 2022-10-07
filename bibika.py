import cv2

img = cv2.imread("6067426786.jpg")
d = g = r = 0
clicked = False
a = 0
s = 0


def color_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global b, r, g, clicked
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        clicked = True


cv2.namedWindow("main")
cv2.setMouseCallback("main", color_function)

while True:
    cv2.imshow("main", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (50, 50), (b, g, r), -1)

    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
