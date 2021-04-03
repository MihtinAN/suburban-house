#!/usr/bin/env python3
import math
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
pygame.init()
FPS = 20
screen = pygame.display.set_mode((610, 610))
pygame.display.set_caption("Tepliche")
clock = pygame.time.Clock()
rect(screen, (255, 255, 255), (10, 10, 590, 590))
done=False
done1=False
portcom1=""
fontObj = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceObj = fontObj.render('Hello world!', True, yellow, blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (500, 400)
pygame.display.flip()
font = pygame.font.Font(None, 30)

textе25 = font.render("com1 com2 com3 com4 com5 com6 com7 com8 com9 com10",True, black, white )
screen.blit(textе25, [10,30])
textе25 = font.render(" com   com   com   com   com   com   com   com   com   com ",True, black, white )
screen.blit(textе25, [10,60])
textе255 = font.render("  11       12       13     14      15      16       17      18      19      20 ",True, black, white )
screen.blit(textе255, [10,80])

textе25 = font.render(" com   com   com   com   com   com   com   com   com   com",True, black, white )
screen.blit(textе25, [10,120])
textе256 = font.render("  21       22       23     24      25      26       27      28      29      30 ",True, black, white )
screen.blit(textе256, [10,140])
textе30 = font.render(" Поехали ",True, black, white )
screen.blit(textе30, [10,400])


pygame.display.update()
comstab = " "
portoppend=0
portoppendnow=0
while not done1:
    clock.tick(FPS)
    textе26 = font.render(comstab+"  " ,True, black, white )
    screen.blit(textе26, [30,250])
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                print (event.pos)
            elif event.button == 1:
                x,y = event.pos
                if x >= 10 and x <= 60 and y >= 10 and  y <= 60:
                    comstab = "COM1"
                    portoppendnow=1
                    portoppend=0
                if x >= 60 and x <= 120 and y >= 10 and  y <= 60:
                    comstab = "COM2"
                    portoppendnow=1
                    portoppend=0
                if x >= 120 and x <= 180 and y >= 10 and  y <= 60:
                    comstab = "COM3"
                    portoppendnow=1
                    portoppend=0
                if x >= 180 and x <= 240 and y >= 10 and  y <= 60:
                    comstab = "COM4"
                    portoppendnow=1
                    portoppend=0
                if x >= 240 and x <= 300 and y >= 10 and  y <= 60:
                    comstab = "COM5"
                    portoppend=0
                if x >= 300 and x <= 360 and y >= 10 and  y <= 60:
                    comstab = "COM6"
                    portoppendnow=1
                    portoppend=0
                if x >= 360 and x <= 420 and y >= 10 and  y <= 60:
                    comstab = "COM7"
                    portoppendnow=1
                    portoppend=0
                if x >= 420 and x <= 480 and y >= 10 and  y <= 60:
                    comstab = "COM8"
                    portoppendnow=1
                    portoppend=0
                if x >= 480 and x <= 540 and y >= 10 and  y <= 60:
                    comstab = "COM9"
                    portoppendnow=1
                    portoppend=0
                if x >= 540 and x <= 600 and y >= 10 and  y <= 60:
                    comstab = "COM10"
                    portoppendnow=1
                    portoppend=0
                if x >= 10 and x <= 60 and y >= 60 and  y <= 120:
                    comstab = "COM11"
                    portoppendnow=1
                    portoppend=0
                if x >= 60 and x <= 120 and y >= 60 and  y <=120:
                    comstab = "COM12"
                    portoppendnow=1
                    portoppend=0
                if x >= 120 and x <= 180 and y >= 60 and  y <= 300:
                    comstab = "COM13"
                    portoppendnow=1
                    portoppend=0
                if x >= 180 and x <= 240 and y >= 10 and  y <= 120:
                    comstab = "COM14"
                    portoppendnow=1
                    portoppend=0
                if x >= 240 and x <= 300 and y >= 60 and  y <= 120:
                    comstab = "COM15"
                    portoppend=0
                if x >= 300 and x <= 360 and y >= 60 and  y <= 120:
                    comstab = "COM16"
                    portoppendnow=1
                    portoppend=0
                if x >= 360 and x <= 420 and y >= 60 and  y <= 120:
                    comstab = "COM17"
                    portoppendnow=1
                    portoppend=0
                if x >= 420 and x <= 480 and y >= 60 and  y <= 120:
                    comstab = "COM18"
                    portoppendnow=1
                    portoppend=0
                if x >= 480 and x <= 540 and y >= 60 and  y <= 120:
                    comstab = "COM19"
                    portoppendnow=1
                    portoppend=0
                if x >= 540 and x <= 600 and y >= 60 and  y <= 120:
                    comstab = "COM20"
                    portoppendnow=1
                    portoppend=0
                if x >= 10 and x <= 60 and y >= 121 and  y <= 160:
                    comstab = "COM21"
                    portoppendnow=1
                    portoppend=0
                if x >= 60 and x <= 120 and y >= 121 and  y <=160:
                    comstab = "COM22"
                    portoppendnow=1
                    portoppend=0
                if x >= 120 and x <= 180 and y >= 121 and  y <= 160:
                    comstab = "COM23"
                    portoppendnow=1
                    portoppend=0
                if x >= 180 and x <= 240 and y >= 121 and  y <= 160:
                    comstab = "COM24"
                    portoppendnow=1
                    portoppend=0
                if x >= 240 and x <= 300 and y >= 121 and  y <= 160:
                    comstab = "COM25"
                    portoppend=0
                if x >= 300 and x <= 360 and y >= 121 and  y <= 160:
                    comstab = "COM26"
                    portoppendnow=1
                    portoppend=0
                if x >= 360 and x <= 420 and y >= 121 and  y <= 160:
                    comstab = "COM27"
                    portoppendnow=1
                    portoppend=0
                if x >= 420 and x <= 480 and y >= 121 and  y <= 160:
                    comstab = "COM28"
                    portoppendnow=1
                    portoppend=0
                if x >= 480 and x <= 540 and y >= 121 and  y <= 160:
                    comstab = "COM29"
                    portoppendnow=1
                    portoppend=0
                if x >= 540 and x <= 600 and y >= 121 and  y <= 160:
                    comstab = "COM30"
                    portoppendnow=1
                    portoppend=0

                if x >= 10 and x <= 600 and y >= 300 and  y <= 600:
                    done1=True
                   

    if portoppend==0 and portoppendnow==1:
        portcom =comstab

        
        try:
            
            ser = serial.Serial(portcom, 9600, timeout = 10)
            portoppend=1
            portoppendnow=0
            #parity=serial.PARITY_EVEN
            #parity = serial.PARITY_ODD
            #, stopbits=serial.STOPBITS_ONE
            #ser=serial.Serial('COM3', 9600, timeout=10)
            #ser=serial.Serial('COM3')
            #ser.baudrate = 9600
            #ser.timeout = 10
            textе26 = font.render("правильный порт           " ,True, black, white )
            screen.blit(textе26, [30,300])
            ser.close()
            portcom1=portcom
        except:
            portoppendnow=0
            portoppend=0
            textе27 = font.render("неправильный сом порт     " ,True, black, white )
            screen.blit(textе27, [30,300])
ser = serial.Serial(portcom1, 9600, timeout = 10)    
#dat1= "1"
#ser = serial.Serial('COM3', 9600)
#data = (bytes(dat1, encoding='ascii'))
#ser.write (data)


# рисует картинку теплици на экране
#выводит в итероктивный режим координаты мышки при нажатии кнопок мыши










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
rect(screen, (0, 0, 0), (220, 450, 130, 40),2)
rect(screen, (0, 0, 0), (107, 205, 49, 230))
rect(screen, (0, 0, 0), (500, 30, 80, 80),2)
# pygame.draw.lines(Surface, color, closed, pointlist, width=1)
#Нарисовать линию, соединяющую точки из последовательности pointlist на поверхности Surface,
#цветом color, с толщиной линии width. Каждая точка представлена парой координат.
#Если параметр closed равен True, конечная точка соединяется с начальной.

pygame.display.update()
clock = pygame.time.Clock()
finished = False
stabtem=" "
rez=" "
ttemp="  "
titem="  "
titem1="  "
xtemp=20
xtemp1=20
clooc=0
sos=1
comreadnum = 0
comread = 0
comread2 = 0
tempin =""
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

while comreadnum <=10 and portoppend==1 and sos==1 : #начальное получение позиций
        print ("читаем sos")
        try:
            ser.write(b'\x31') # так отправляем в сом порт ff
            time.sleep(0.2)
            comread  =ser.read(ser.inWaiting())# ser.readline() #reading up to 1 bytes
            print (len(comread))
            if (len(comread)) == 5:
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
               # print (comread[5])
               # print (comread[6])
               # print (comread[7])
               # print (comread[8])
                sinxr = chr(comread[0])+chr (comread[1])+chr (comread[2])
                do1 = chr (comread[0])
                pec = chr (comread[1])
                foo = chr (comread[2])
                print(do1,pec,foo)
                if comread[0] == 49:
                    door = True
                    door1 = True
                elif comread[0] == 48 :
                    door = False
                    door1 = False
                if comread[1] == 49:
                    pech = True
                    pech1 = True
                elif comread[1] == 48 :
                    pech = False
                    pech1 = False
                if comread[2] == 49:
                    fort = True
                    fort1 = True
                elif comread[2] == 48 :
                    fort = False
                    fort1 = False
                


                print(door,pech,fort)
        except:
            print ("неправильный сом порт состояния")
        comreadnum += 1 
        

while not finished:
    clock.tick(FPS)
    if clooc==20:
        clooc=0
    clooc +=1
    comreadnum = 0
   
    print ("модуль" +str(clooc)+"_"+str(comreadnum )+"_"+str(portoppend)+"_"+str(sos))



    try:
        if clooc==4 and portoppend==1 and sos==1  : #получаем температуру 
            ser.write(b'\x32') # так отправляем в сом порт ff
            time.sleep(0.1)
            comread2 = ser.read(ser.inWaiting()) #reading up to 1 bytes
            print (comread2)
            print (len(comread2))
            if (len(comread2)) == 4:    
                print (comread2[0])
                print (comread2[1])
                print (comread2[2])
                print (comread2[3])
                #print (comread2[4])
               # print (comread2[5])
               # print (comread2[6])
               # print (comread2[7])
                ttemp="good4"
                tempin =(chr (comread2[0])+chr (comread2[1]))                       
    except:
        print ("неправильный сом порт темературы")       
    if clooc==14:               # получение позиций

        while   comreadnum <=10 and portoppend==1 and sos==1  :
            print ("модуль14"+"_" +str(comreadnum )+"_" +str(portoppend)+"_" +str(sos))
            try:
                ser.write(b'\x31') # так отправляем в сом порт ff
                time.sleep(0.2)
                comread  =ser.read(ser.inWaiting())# ser.readline() #reading up to 1 bytes
                print (len(comread))
                if (len(comread)) == 5:
                    comreadnum = 11
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
                    #print (comread[5])
                    #print (comread[6])
                    #print (comread[7])
                    #print (comread[8])
                    sinxr = chr(comread[0])+chr (comread[1])+chr (comread[2])
                    do1 = chr (comread[0])
                    pec = chr (comread[1])
                    foo = chr (comread[2])
                    print(do1,pec,foo)
                    if comread[0] == 49:
                        door = True
                        door1 = True
                    elif comread[0] == 48 :
                        door = False
                        door1 = False
                    if comread[1] == 49:
                        pech = True
                        pech1 = True
                    elif comread[1] == 48 :
                        pech = False
                        pech1 = False
                    if comread[2] == 49:
                        fort = True
                        fort1 = True
                    elif comread[2] == 48 :
                        fort = False
                        fort1 = False
                

                    titem="good14"
                    print(door,pech,fort)
            except:
                print ("неправильный сом порт состояния")
    if clooc==2:
           #повторное получение позиций
        while comreadnum <=10 and portoppend==1 and sos==1:
            print ("читаем sos3")
            try:
                comreadnum = 11
                titem1="good17"
                print ("читаем sos1") 
                print ("читаем темпер. стабилизациии режим.")
                ser.write(b'\x01') # так отправляем в сом порт 01
                time.sleep(0.1)
                stabtemprez  =ser.readline() #reading up to 1 bytes
                print (stabtemprez)
                print (len(stabtemprez))
                if (len(stabtemprez)) == 5:    
                    print (stabtemprez[0])
                    print (stabtemprez[1])
                    print (stabtemprez[2])
                    print (stabtemprez[3])
                    print (stabtemprez[4])
                    stabtem =chr (stabtemprez[0])+chr (stabtemprez[1])
                    print ("температура стабилизации"+stabtem)
                    rez= chr(stabtemprez[2])
                    print ("режим"+rez)

                                        
            except:
                print ("неправильный сом порт1")
        
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
    textе2 = font.render("температура "+tempin,True, black, white )
    screen.blit(textе2, [25,50])
    #textе22 = font.render("модули"+ttemp+titem+titem1,True, black, white )
    #screen.blit(textе22, [200,50])
    textе3 = font.render("15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33  ",True, black, white )
    screen.blit(textе3, [30,550])

    textе24 = font.render("Закупорить ",True, black, white )
    screen.blit(textе24, [230,470])

    textе23 = font.render("темп.стаб "+stabtem+"режим"+rez,True, black, white )
    screen.blit(textе23, [25,70])
    pygame.display.update()

    
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
            
            
       
    for event in pygame.event.get(): 
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
                
                elif x >= 250 and x <= 450 and y >= 300 and  y <= 550:
                    print ("закупорить ")

                    try:
                        ser.write(b'\x02') # так отправляем в сом порт 02
                    except:
                        print ("неправильный сом порт") 







                elif x >= 500 and x <= 599 and y >= 30 and  y <= 130:
                    read1 = True
                    print ("читаем")
                    try:
                        

                        ser.write(b'\x31') # так отправляем в сом порт ff
                        time.sleep(0.2)

                        comread  =ser.read(ser.inWaiting())# ser.readline() #reading up to 1 bytes
                        print (len(comread))


                        if (len(comread)) == 5:
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
                          # print (comread[5])
                           #print (comread[6])
                          # print (comread[7])
                          # print (comread[8])
                           sinxr = chr(comread[0])+chr (comread[1])+chr (comread[2])
                           print (sinxr)
                    except:
                        print ("неправильный сом порт")
                        
                elif x >= 500 and x <= 599 and y >= 130 and y <= 230:
                                     
                    read1 = False
                    print ("читаем")
                    try:
                        

                        ser.write(b'\x32') # так отправляем в сом порт ff
                        time.sleep(0.1)
                        comread2 = ser.readline() #reading up to 1 bytes
                        print (comread2)
                        print (len(comread2))
                        if (len(comread2)) == 4:    
                            print (comread2[0])
                            print (comread2[1])
                            print (comread2[2])
                            print (comread2[3])
                            tempin =(chr (comread2[0])+chr (comread2[1]))
                            print ("температура"+(tempin))

                                        
                    except:
                        print ("неправильный сом порт1")


                elif x >= 30 and x <= 570 and y >= 540 and y <= 580:    #30.550

                    xtemp1 = xtemp
                    xtemp = math.trunc((x-30)/28)+15                  
                    print (xtemp1,xtemp)
                    print ("Устанавливаю температуру"+str(xtemp))
                    if xtemp != xtemp1:
                        print ("движение")
                        xxtemp =2+(xtemp-14)*28
                        xxtemp1 =2+(xtemp1-14)*28 
                        rect(screen, (255, 255, 255), (xxtemp1, 540, 28, 10),1)
                        rect(screen, (0, 0, 0), (xxtemp, 540, 28, 10),1)
                        xtemp1 = xtemp
                        pygame.display.update()
                         

                    #read1 = False
                    #print ("читаем")
                    try:
                        if xtemp == 15:
                            ser.write(b'\x34') # так отправляем в сом порт ff
                        elif xtemp == 16:
                            ser.write(b'\x35') # так отправляем в сом порт ff
                        elif xtemp == 17:
                            ser.write(b'\x36') # так отправляем в сом порт ff
                        elif xtemp == 18:
                            ser.write(b'\x37') # так отправляем в сом порт ff
                        elif xtemp == 19:
                            ser.write(b'\x38') # так отправляем в сом порт ff
                        elif xtemp == 20:
                            ser.write(b'\x39') # так отправляем в сом порт ff
                        elif xtemp == 21:
                            ser.write(b'\x3a') # так отправляем в сом порт ff
                        elif xtemp == 22:
                            ser.write(b'\x3b') # так отправляем в сом порт ff
                        elif xtemp == 23:
                            ser.write(b'\x3c') # так отправляем в сом порт ff
                        elif xtemp == 24:
                            ser.write(b'\x3d') # так отправляем в сом порт ff
                        elif xtemp == 25:
                            ser.write(b'\x3e') # так отправляем в сом порт ff
                        elif xtemp == 26:
                            ser.write(b'\x3f') # так отправляем в сом порт ff
                        elif xtemp == 27:
                            ser.write(b'\x40') # так отправляем в сом порт ff
                        elif xtemp == 28:
                            ser.write(b'\x41') # так отправляем в сом порт ff
                        elif xtemp == 29:
                            ser.write(b'\x42') # так отправляем в сом порт ff
                        elif xtemp == 30:
                            ser.write(b'\x43') # так отправляем в сом порт ff
                        elif xtemp == 31:
                            ser.write(b'\x44') # так отправляем в сом порт ff
                        elif xtemp == 32:
                            ser.write(b'\x45') # так отправляем в сом порт ff
                        elif xtemp == 33:
                            ser.write(b'\x46') # так отправляем в сом порт ff
                        elif xtemp == 33:
                            ser.write(b'\x47') # так отправляем в сом порт ff

                        time.sleep(0.1)
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
