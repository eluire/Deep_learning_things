#especificações feitas para a camera do drone dji spark
#resolução do video 1920 x 1080
import sys
import numpy as np
import matplotlib as plt
import cv2
import math

# pegar flags do terminal
freme = sys.argv[1]
txt = sys.argv[2]

#calcular distancia entre pontos
def convert_to_pixel_x(x):
    x = float(x)
    pixels_x = (x*1920)/0.999479
    return int(pixels_x)

def convert_to_pixel_y(y):
    y = float(y)
    pixels_y = (y*1080)/0.999074
    return int(pixels_y)

def distance(x1,y1,x2,y2):
    dist = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 3)
    return dist

def mediumPointline(x1, x2, y1, y2):
    xm = int((x1+y2)/2)
    ym = int((y1+x2)/2)
    return (x1+200, y2)

def rectangle_coordinates(xmed,ymed,width,heigth):
    #calculos dos vertices do retangulo para usar no cv2.rectangle
    extreme_bottom_x = xmed - (width/2)
    extreme_bottom_y = ymed - (heigth/2)
    extreme_top_x = xmed + (width/2)
    extreme_top_y = ymed + (heigth/2)

    extreme_points_rectangle = ((int(extreme_bottom_x),int(extreme_bottom_y)),(int(extreme_top_x),int(extreme_top_y)))
    return extreme_points_rectangle

#def velocidade():


#A =

#atribuido as variáveis para os calculos


#definindo dicionario com os atributos de uma box e salvando os informaçoes de cada box em uma lista
coisas_da_imagem = {
    'class': [],
    'x_centroid': [],
    'y_centroid': [],
    'width': [],
    'heigth': []
}
# leitura do txt e splitando nos atributos definidos anteriormente
file  = open(txt,"r")
for line in file:

    field = line.split(" ")
    field[-1] = field[-1][0:-1]


    coisas_da_imagem['class'].append(field[0])
    coisas_da_imagem['x_centroid'].append(convert_to_pixel_x(field[1]))
    coisas_da_imagem['y_centroid'].append(convert_to_pixel_y(field[2]))
    coisas_da_imagem['heigth'].append(convert_to_pixel_y(field[3]))
    coisas_da_imagem['width'].append(convert_to_pixel_x(field[4]))

file.close()

# desenhar linhas entre pontos


print(coisas_da_imagem['x_centroid'][0], coisas_da_imagem['y_centroid'][0], coisas_da_imagem['x_centroid'][1], coisas_da_imagem['y_centroid'][1])



img = cv2.imread('/home/mateus/Imagens/frame55.jpg')

cv2.line(img, (coisas_da_imagem['x_centroid'][0],coisas_da_imagem['y_centroid'][0]), (coisas_da_imagem['x_centroid'][1],coisas_da_imagem['y_centroid'][1]), (0, 0, 255), 3)
# colocar texto da distancia
cv2.putText(
    img,
    str(distance(coisas_da_imagem['x_centroid'][0],coisas_da_imagem['y_centroid'][0],coisas_da_imagem['x_centroid'][1],coisas_da_imagem['y_centroid'][1])),
    mediumPointline(
        coisas_da_imagem['x_centroid'][0],
        coisas_da_imagem['y_centroid'][0],
        coisas_da_imagem['x_centroid'][1],
        coisas_da_imagem['y_centroid'][1]
    ),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,(255, 255, 255),2,
    cv2.LINE_AA
 )
 # colocar retangulos nos carros
cv2.rectangle(
    img,
    rectangle_coordinates(coisas_da_imagem['x_centroid'][0],coisas_da_imagem['y_centroid'][0],coisas_da_imagem['width'][0],coisas_da_imagem['heigth'][0])[0],
    rectangle_coordinates(coisas_da_imagem['x_centroid'][0],coisas_da_imagem['y_centroid'][0],coisas_da_imagem['width'][0],coisas_da_imagem['heigth'][0])[1],
    (0,255,0),3
 )
cv2.rectangle(
     img,
    rectangle_coordinates(coisas_da_imagem['x_centroid'][1],coisas_da_imagem['y_centroid'][1],coisas_da_imagem['width'][1],coisas_da_imagem['heigth'][1])[0],
    rectangle_coordinates(coisas_da_imagem['x_centroid'][1],coisas_da_imagem['y_centroid'][1],coisas_da_imagem['width'][1],coisas_da_imagem['heigth'][1])[1],
     (0,255,0),3
  )

win = 'Mid Point Line'
cv2.namedWindow(win, cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(win, 1058, 595)
cv2.imshow(win, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
