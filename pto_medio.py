#especificações feitas para a camera do drone dji spark
#resolução do video 1920 x 1080
import numpy as np
import matplotlib as plt
import cv2
import math

#calcular distancia entre pontos
def convert_to_pixel_x(x):
    pixels_x = (x*1920)/0.999479
    return int(pixels_x)

def convert_to_pixel_y(y):
    pixels_y = (y*1080)/0.999074
    return int(pixels_y)

def distance(x1,y1,x2,y2):
    dist = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 3)
    return dist

def mediumPoint(x1, x2, y1, y2):
    xm = int((x1+x2)/2) - 100
    ym = int((y1+y2)/2)

    return (xm, ym)

x1 = convert_to_pixel_x(0.348958)
y1 = convert_to_pixel_y(0.690741)
x2 = convert_to_pixel_x(0.628646)
y2 = convert_to_pixel_y(0.691204)

print(distance(x1,y1,x2,y2))

# desenhar linhas entre pontos

img = cv2.imread('/home/mateus/Imagens/frame55.jpg')

cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 3)
cv2.putText(
    img,
    str(distance(x1,y1,x2,y2)),
    mediumPoint(x1, x2, y1, y2),
    cv2.FONT_HERSHEY_SIMPLEX, 2,
    (255, 255, 255), 2 , cv2.LINE_AA
 )

win = 'Mid Point Line'
cv2.namedWindow(win, cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(win, 1058, 595)
cv2.imshow(win, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
