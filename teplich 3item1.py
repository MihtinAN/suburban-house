#!/usr/bin/env python3
import pygame
from pygame.draw import *
# рисует картинку теплици на экране
#выводит в итероктивный режим координаты мышки при нажатии кнопок мыши
pygame.init()

FPS = 30
screen = pygame.display.set_mode((610, 610))

#rect(Surface, color, Rect, width=0) -> Rect
#Rect((left, top), (width, height))

rect(screen, (255, 255, 255), (10, 10, 590, 590))

pygame.draw.line(screen,(0, 0, 0), (10, 170), (180, 10), 2)
pygame.draw.line(screen,(0, 0, 0), (420, 10), (600, 170), 2)
rect(screen, (0, 0, 0), (170, 190, 280, 250), 2)
#нарисовали крышу
pygame.draw.line(screen,(0, 0, 0), (10, 170), (170, 190), 2)
pygame.draw.line(screen,(0, 0, 0), (450, 190), (600, 170), 2)

#рисум стропилы
pygame.draw.line(screen,(0, 0, 0), (90,180), (280, 30), 2)
pygame.draw.line(screen,(0, 0, 0), (280,30), (340, 30), 2)
pygame.draw.line(screen,(0, 0, 0), (340, 30), (520, 180), 2)

pygame.draw.line(screen,(0, 0, 0), (133, 186), (297, 79), 2)
pygame.draw.line(screen,(0, 0, 0), (297, 79), (317, 79), 2)
pygame.draw.line(screen,(0, 0, 0), (317, 79), (482, 185), 2)
pygame.draw.line(screen,(0, 0, 0), (172, 186), (305, 120), 2)
pygame.draw.line(screen,(0, 0, 0), (305, 120), (452, 188), 2)
pygame.draw.line(screen,(0, 0, 0), (172, 186), (305, 120), 2)
pygame.draw.line(screen,(0, 0, 0), (305, 120), (452, 188), 2)
# нарисовали столпила

# рисуем основыние теплици
pygame.draw.line(screen,(0, 0, 0), (11, 578), (170, 440), 2)
pygame.draw.line(screen,(0, 0, 0), (10, 597), (172, 449), 2)
pygame.draw.line(screen,(0, 0, 0), (172, 446), (447, 446), 2)
pygame.draw.line(screen,(0, 0, 0), (451, 440), (600, 580), 2)
pygame.draw.line(screen,(0, 0, 0), (446, 446), (603, 600), 2)

# рисуем окна на левой стороне
pygame.draw.line(screen,(0, 0, 0), (18, 555), (18, 189), 2)
pygame.draw.line(screen,(0, 0, 0), (18, 189), (71, 194), 2)
pygame.draw.line(screen,(0, 0, 0), (71, 194), (71, 506), 2)
pygame.draw.line(screen,(0, 0, 0), (71, 506), (18, 555), 2)

# дверка в закрытом виде как окно 
pygame.draw.line(screen,(0, 0, 0), (88, 197), (158, 203) , 2)
pygame.draw.line(screen,(0, 0, 0), (158, 203), (159, 435), 2)
pygame.draw.line(screen,(0, 0, 0), (159, 435), (92, 489) , 2)
pygame.draw.line(screen,(0, 0, 0), (92, 489) ,  (88, 197), 2)

# рисуем окно на правой стороне
pygame.draw.line(screen,(0, 0, 0), (460, 203), (511, 196), 2)
pygame.draw.line(screen,(0, 0, 0), (511, 196), (511, 479), 2)
pygame.draw.line(screen,(0, 0, 0), (511, 479), (459, 436), 2)
pygame.draw.line(screen,(0, 0, 0), (459, 436), (460, 203), 2)

pygame.draw.line(screen,(0, 0, 0), (521, 488), (521, 195), 2)
pygame.draw.line(screen,(0, 0, 0), (521, 195), (587, 187), 2)
pygame.draw.line(screen,(0, 0, 0), (587, 190), (589, 549), 2)
pygame.draw.line(screen,(0, 0, 0), (589, 549), (521, 488), 2)

# рисуем окно на правой стороне
rect(screen, (0, 0, 0), (203, 237, 70, 60), 2)
rect(screen, (0, 0, 0), (203, 371, 70, 60), 2)
# рисуем вентиляцию на крыне 

pygame.draw.line(screen,(0, 0, 0), (310, 86), (400, 139), 2)
pygame.draw.line(screen,(0, 0, 0), (400, 139), (372, 146), 2)
pygame.draw.line(screen,(0, 0, 0), (372, 146), (313, 118), 2)
pygame.draw.line(screen,(0, 0, 0), (313, 118), (310, 86), 2)

rect(screen, (0, 0, 0), (107, 205, 49, 230))

# pygame.draw.lines(Surface, color, closed, pointlist, width=1)
#Нарисовать линию, соединяющую точки из последовательности pointlist на поверхности Surface,
#цветом color, с толщиной линии width. Каждая точка представлена парой координат.
#Если параметр closed равен True, конечная точка соединяется с начальной.

pygame.display.update()
clock = pygame.time.Clock()
finished = False
door = False    # переменная двери
pech = False     # пременная окна печки
fort = False      # переменная форточки в крыше 
while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if door == True: # проверяем состояние двери перерисовываем дверь
            rect(screen, (0, 0, 0), (107, 205, 49, 230))
            pygame.display.update()
        else:
            rect(screen, (255, 255, 255), (107, 205, 49, 230))
            pygame.display.update()
        if pech == True: # проверяем состояние окна печки перерисоваваем окно печки
            rect(screen, (0, 0, 0), (203, 237, 70, 60))
            rect(screen, (0, 0, 0), (203, 371, 70, 60))
            pygame.display.update()
        else:
            rect(screen, (255, 255, 255), (205, 239, 68, 56))
            rect(screen, (255, 255, 255), (205, 373, 68, 57))
            pygame.display.update()    
        if fort == False: # проверяем состояние форточки переисоваваем форточку двумя треугольниками
           
            pygame.draw.polygon(screen, (255, 255, 255) , ( (312, 88), (398, 139), (370, 144)) )
            pygame.draw.polygon(screen, (255, 255, 255) , ( (312, 88), (315, 116), (370, 144) ) )
            pygame.display.update()
        else:
       
            pygame.draw.polygon(screen, (0, 0, 0) , ( (310, 86), (400, 139), (372, 146)) )
            pygame.draw.polygon(screen, (0, 0, 0) , ( (312, 86), (313, 117), (373, 146) ) )
            pygame.display.update() 
       



        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                print (event.pos)
            elif event.button == 1:
                x,y = event.pos
                if x >= 107 and x <= 153 and y >= 204 and  y <= 431:
                   if door == True:
                       door = False
                   else:
                       door = True
                elif x >= 202 and x <= 272 and y >= 236 and  y <= 296:
                    if  pech == False:
                        pech = True
                    else:
                        pech = False
                elif x >= 315 and x <= 404 and y >= 85 and  y <= 149:
                    if  fort == False:
                        fort = True
                    else:
                        fort = False        

pygame.quit()
