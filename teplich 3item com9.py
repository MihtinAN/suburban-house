#!/usr/bin/env python3
import time
import serial
import pygame
from pygame.draw import *
import pickle
aqua      = (  0, 255, 255)   # морская волна
black     = (  0,   0,   0)   # черный      
blue      = (  0,   0, 255)   # синий       
fuchsia   = (255,   0, 255)   # фуксия      
gray      = (128, 128, 128)   # серый       
green     = (  0, 128,   0)   # зеленый     
lime      = (  0, 255,   0)   # цвет лайма  
maroon    = (128,   0,   0)   # темно-бордовый
navy_blue = (  0,   0, 128)   # темно-синий 
olive     = (128, 128,   0)   # оливковый   
purple    = (128,   0, 128)   # фиолетовый  
red       = (255,   0,   0)   # красный     
silver    = (192, 192, 192)   # серебряный  
teal      = (  0, 128, 128)   # зелено-голубой
white     = (255, 255, 255)   # белый       
yellow    = (255, 255,   0)   # желтый       



try:
    ser = serial.Serial('COM3', 9600, timeout = 10)
    #parity=serial.PARITY_EVEN
    #parity = serial.PARITY_ODD
    #, stopbits=serial.STOPBITS_ONE
    #ser=serial.Serial('COM3', 9600, timeout=10)
    #ser=serial.Serial('COM3')
    #ser.baudrate = 9600
    #ser.timeout = 10
except:
    print ("неправильный сом порт") 
#dat1= "1"
#ser = serial.Serial('COM3', 9600)
#data = (bytes(dat1, encoding='ascii'))
#ser.write (data)


# рисует картинку теплици на экране
#выводит в итероктивный режим координаты мышки при нажатии кнопок мыши
pygame.init()

FPS = 30
screen = pygame.display.set_mode((610, 610))
pygame.display.set_caption("Tepliche")
done=False




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
rect(screen, (0, 0, 0), (500, 30, 80, 80),2)
# pygame.draw.lines(Surface, color, closed, pointlist, width=1)
#Нарисовать линию, соединяющую точки из последовательности pointlist на поверхности Surface,
#цветом color, с толщиной линии width. Каждая точка представлена парой координат.
#Если параметр closed равен True, конечная точка соединяется с начальной.

pygame.display.update()
clock = pygame.time.Clock()
finished = False
comreadnum = 0
comread = 0
sinxr =""
read1 = True  #флаг чтения
door1 = False    # переменная двери
pech1 = False     # пременная окна печки
fort1 = False      # переменная форточки в крыше 
file1 = open('sostep.txt' ,'w')
doorstr = "door "
pechstr = "pech "
fortstr = "fort "
openstr = "open "
closestr= "close "
summasrt = ""
sobitie = False  # переменная переменая говорит о том что было событие в последнем цыкле 
door = False    # переменная двери
pech = False     # пременная окна печки
fort = False      # переменная форточки в крыше 

while comreadnum <=10:
        print ("читаем")
        try:
            ser.write(b'\x31') # так отправляем в сом порт ff
            time.sleep(0.2)
            comread  =ser.read(ser.inWaiting())# ser.readline() #reading up to 1 bytes
            print (len(comread))
            if (len(comread)) == 9:
                comreadnum += 10
                #door = True
                #pech = True
                #fort = True
                print (comread)
                print ("синхронезировано")
                print (comread[0])
                print (comread[1])
                print (comread[2])
                print (comread[3])
                print (comread[4])
                print (comread[5])
                print (comread[6])
                print (comread[7])
                print (comread[8])
                sinxr = chr(comread[4])+chr (comread[5])+chr (comread[6])
                do1 = chr (comread[4])
                pec = chr (comread[5])
                foo = chr (comread[6])
                print(do1,pec,foo)
                if comread[4] == 49:
                    door = True
                    door1 = True
                elif comread[4] == 48 :
                    door = False
                    door1 = False
                if comread[5] == 49:
                    pech = True
                    pech1 = True
                elif comread[5 == 48] :
                    pech = False
                    pech1 = False
                if comread[6] == 49:
                    fort = True
                    fort1 = True
                elif comread[6] == 48 :
                    fort = False
                    fort1 = False
                


                print(door,pech,fort)
        except:
            print ("неправильный сом порт")
        comreadnum += 1 


while not finished:
    clock.tick(FPS)
    sobitie = False
    summasrt =""
    



    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Hello world!', True, yellow, blue)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (500, 400)
    pygame.display.flip()
    font = pygame.font.Font(None, 30)
    
    text = font.render("My text",True,black)
    rect(screen, (white), (10, 10, 30, 100))
    score = sinxr
    text = font.render("состояние ард. ",True,black ,white )
    screen.blit(text, [15,15])
    text = font.render("My text",True,black)
    textе = font.render(" ард. "+str(score),True, black, white )
    screen.blit(textе, [25,30])




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

                elif x >= 500 and x <= 599 and y >= 30 and  y <= 130:
                    read1 = True
                    print ("читаем")
                    try:
                        

                        ser.write(b'\x31') # так отправляем в сом порт ff
                        time.sleep(0.2)

                        comread  =ser.read(ser.inWaiting())# ser.readline() #reading up to 1 bytes
                        print (len(comread))


                        if (len(comread)) == 9:
                           #door = True
                           #pech = True
                           #fort = True
                           print (comread)
                           print ("синхронезировано")
                           print (comread[0])
                           print (comread[1])
                           print (comread[2])
                           print (comread[3])
                           print (comread[4])
                           print (comread[5])
                           print (comread[6])
                           print (comread[7])
                           print (comread[8])
                           sinxr = chr(comread[4])+chr (comread[5])+chr (comread[6])
                    except:
                        print ("неправильный сом порт")
                        
                elif x >= 500 and x <= 599 and y >= 130 and y <= 230:
                     
                    read1 = False
                    print ("читаем")
                    try:
                        

                        ser.write(b'\x32') # так отправляем в сом порт ff
                        time.sleep(0.1)
                        comread = ser.readline() #reading up to 1 bytes
                        
                            
                        

                        
                    except:
                        print ("неправильный сом порт")             
                if door == False:
                     if door1 == True:
                        door1 = False
                        sobitie = True
                        try:        
                            ser.write(b'\x0a') # так отправляем в сом порт 0а
                        except:
                            print ("неправильный сом порт") 

                else:
                     if door1 == False:
                        door1 = True
                        sobitie = True
                        try:
                            ser.write(b'\x1a') # так отправляем в сом порт 1а
                        except:
                            print ("неправильный сом порт") 
                            
                if pech == False:
                     if pech1 == True:
                        pech1 = False
                        sobitie = True
                        try:
                            ser.write(b'\x0b') # так отправляем в сом порт 0b
                        except:
                             print ("неправильный сом порт")                             
                else:
                     if pech1 == False:
                        pech1 = True
                        sobitie = True
                        try:
                            ser.write(b'\x1b') # так отправляем в сом порт 1b
                        except:
                            print ("неправильный сом порт") 
                if fort == False :
                    if fort1 == True:
                        fort1 = False
                        sobitie = True
                        try:            
                            ser.write(b'\x0c') # так отправляем в сом порт 0с
                        except:
                            print ("неправильный сом порт") 
                else:
                    if fort1 == False:
                        fort1 = True
                        sobitie = True
                        try:
                            ser.write(b'\x1c') # так отправляем в сом порт 1c
                        except:
                            print ("неправильный сом порт")
                
                if sobitie == True:
                   if door == False:
                     summasrt =summasrt + doorstr + closestr
                   else:
                       summasrt =summasrt + doorstr + openstr
                   if pech == False:
                       summasrt =summasrt + pechstr + closestr
                   else:
                       summasrt =summasrt + pechstr + openstr
                   if fort == False:
                       summasrt =summasrt + fortstr + closestr
                   else:
                       summasrt =summasrt + fortstr + openstr
                   print(door,pech,fort)     
                   print(door1,pech1,fort1) 
                   print(summasrt)
                   file1 = open('sostep.txt' ,'w')
                   file1.write(summasrt)
                   file1.close()
                   data = [door,pech,fort]
                   with open('data.pickle', 'wb') as f:
	                    pickle.dump (data, f) 
	                
                   
pygame.quit()
