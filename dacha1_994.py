
import math
import time
import serial
import pygame
from pygame.draw import *
import pickle
pygame.init()
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

def cursor(x,y):            #определяем где произошло сабытие
    if x>=300 and x<=900 and y>=10 and y<=600:
        return "scena"
    elif x>=26 and x<=286 and y>=19 and y<=73:
        return "0"
    elif x>=26 and x<=286 and y>=88 and y<=142:
        return "1"
    elif x>=26 and x<=286 and y>=160 and y<=212:
        return "2"
    elif x>=26 and x<=286 and y>=228 and y<=282:
        return "3"
    elif x>=300 and x<=900 and y>=607 and y<=700:
        return "nizniy"
    return "nezn"






class Scena:
    #зисуем сцену
    def __init__(self,x,y,itname1=" ",itname2=" ",itname3=" ",name=" ",rend=0 ):
        self. item1 = 0    # переменная двери
        self. item2 = 0     # пременная окна печки
        self. item3 = 0      # переменная форточки в крыше
        self.itname1=itname1
        self.itname2=itname2
        self.itname3=itname3

        Scena.nacalox = x
        Scena.nacaloy = y
        if rend==1: 
            self.drawscene(x,y,name)
            self.name=name
            print(self)


    def drawtempset(self ):             #пичатаем строку температур
        textе31 = font.render("15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33  ",True, black, white )
        screen.blit(textе31, [30+Scena.nacalox ,550])
    def prrintstabterm(self ):
        try:
            textе23 = font.render("темп.стаб"+tepl.stabtem+"режим"+tepl.rez,True, black, white )
            screen.blit(textе23, [25+Scena.nacalox ,70])
            pygame.display.update()
        except:
            print("данные еше не получены")
    def settempstab(self):          # вычитаем температуру то температурной строке
        
        self. xtemp1 =self.xtemp
        self. xtemp = math.trunc(((Scena.x1-Scena.nacalox)-30)/28)+15                  
        print (self. xtemp1,self. xtemp)
        print ("Устанавливаю температуру"+str(self .xtemp))
        if self.xtemp != self.xtemp1:
            print ("движение")
            self.xxtemp =(2+(self.xtemp-14)*28)+Scena.nacalox
            self.xxtemp1 =(2+(self.xtemp1-14)*28)+Scena.nacalox 
            rect(screen, (255, 255, 255), (self. xxtemp1, 540, 28, 10),1)
            rect(screen, (0, 0, 0), (self. xxtemp, 540, 28, 10),1)
            self.xtemp1 = self.xtemp
            pygame.display.update()
            return int(self.xtemp)
    def sobitiescen(self):          #ветвление событий в зависимости от каординат

        if self == tepl:

            if Scena.x1 >= 107 + Scena.nacalox and Scena.x1 <= 153 + Scena.nacalox and Scena.y1 >= 204 and Scena.y1 <= 431:
                #textе233 = font.render("Дверь " + str(self.item1) , True, black, white)
                #screen.blit(textе233, [25, 500])

                if self. item1 == 0:
                    self. item1 = 1
                else:
                    self. item1 =0
                #textе235 = font.render("Дверь " + str(self.item1), True, black, white)
                #screen.blit(textе235, [180, 500])
                teplp.write_item(1)

            if Scena.x1 >= 202 + Scena.nacalox and Scena.x1 <= 272 + Scena.nacalox and Scena.y1 >= 236 and Scena.y1 <= 296:
                #textе236 = font.render("Печка " + str(self.item2), True, black, white)
                #screen.blit(textе236, [25, 520])

                if self.item2 == 0:
                    self.item2 = 1
                else:
                    self.item2 = 0
                #textе237 = font.render("Печка " + str(self.item2), True, black, white)
                #screen.blit(textе237, [180, 520])
                teplp.write_item(2)

            if Scena.x1 >= 315 + Scena.nacalox and Scena.x1 <= 404 + Scena.nacalox and Scena.y1 >= 85 and Scena.y1 <= 149:
                #textе238 = font.render("Форточка " + str(self.item3), True, black, white)
                #screen.blit(textе238, [25, 540])
                if self.item3 == 0:
                    self.item3 = 1
                else:
                    self.item3 = 0
                #textе249 = font.render("Форточка " + str(self.item3), True, black, white)
                #screen.blit(textе249, [180, 540])
                teplp.write_item(3)
            textе232 = font.render(str(self.item1)+str(self.item3)+str(self.item3), True, black, white)
            screen.blit(textе232, [25 , 620])
            print ( self.item1,self.item2,self.item3)
            if Scena.x1 >= 20 + Scena.nacalox and Scena.x1 <= 570 + Scena.nacalox and Scena.y1 >= 550 and Scena.y1 <= 570:
                avtotemp=tepl.settempstab()
                print(avtotemp)
                textе250 = font.render("Температура стабилизации " + str(self.xtemp), True, black, white)
                screen.blit(textе250, [200+Scena.nacalox , 580])
                teplp.set_tempstabrez()
            if Scena.x1 >= 220 + Scena.nacalox and Scena.x1 <= 470 + Scena.nacalox and Scena.y1 >= 440 and Scena.y1 <= 500:
                teplp.zakuporit()




        #try:
                    #textе37 = font.render("отправляем в порт закупорить", True, black, white)
                    #screen.blit(textе37, [10, 650])
                    #pygame.display.update()

                    # ser.write(b'\x02') # так отправляем в сом порт 02
                #except:
                    #print("неправильный сом порт")


    def sowsust(self):        #перерисрвываем двери форточки печку на сценев зависимости от итем по событию
        if self == tepl:
            if self. item1 == 1: # проверяем состояние двери перерисовываем дверь
                rect(screen, (0, 0, 0), (107+Scena.nacalox , 206, 49, 230))
                pygame.display.update()

            else:
                rect(screen, (255, 255, 255), (107+Scena.nacalox , 206, 49, 230))
                pygame.display.update()
            
            if self. item2 == 1: # проверяем состояние окна печки перерисоваваем окно печки
                rect(screen, (0, 0, 0), (203+Scena.nacalox , 238, 70, 60))
                rect(screen, (0, 0, 0), (203+Scena.nacalox , 372, 70, 60))
                pygame.display.update()
            
            
            
            else:
                rect(screen, (255, 255, 255), (205+Scena.nacalox , 240, 68, 56))
                rect(screen, (255, 255, 255), (205+Scena.nacalox , 374, 68, 57))
                pygame.display.update()
            
            
            if self. item3 == 1: # проверяем состояние форточки переисоваваем форточку двумя треугольниками
           
                pygame.draw.polygon(screen, (0, 0, 0) , ( (312+Scena.nacalox , 89), (398+Scena.nacalox , 140), (370+Scena.nacalox , 145)) )
                pygame.draw.polygon(screen, (0, 0, 0) , ( (312+Scena.nacalox , 89), (315+Scena.nacalox , 117), (370+Scena.nacalox , 145) ) )
                pygame.display.update()
            
            else:
       
                pygame.draw.polygon(screen, (255, 255, 255) , ( (311+Scena.nacalox , 89), (400+Scena.nacalox , 142), (372+Scena.nacalox , 149)) )
                pygame.draw.polygon(screen, (255, 255, 255) , ( (313+Scena.nacalox , 89), (313+Scena.nacalox , 120), (373+Scena.nacalox , 149) ) )
                pygame.display.update()
            
            
        elif self ==signal:
            print (self)
        elif self ==voda:
            print (self)
        elif self ==came:
            print (self)
            

    def pererisovka():
       if Scena.activmenu1 != Scena.activmenu:
           print("перерисовка"+Scena.activmenu1+"  "+Scena.activmenu)
           Scena.activmenu1 = Scena.activmenu
           Scena.drawscene(activ,295,2,Scena.activmenu)
           
    def drawscene(self,x,y,name,):      # рисуем сцену взависимости от переменой активности окна
        #rect(Surface, color, Rect, width=0) -> Rect
        #Rect((left, top), (width, height))
        if  name=="0":
            self.nacalox = x
            self.nacaloy = y
            rect(screen, (white), (10+self.nacalox, 10+self.nacaloy , 590, 590),)
            rect(screen, (0, 0, 0), (10+self.nacalox, 10+self.nacaloy , 590, 590),5)
        

            pygame.draw.line(screen,(0, 0, 0), (10 +self.nacalox, 170+self.nacaloy ), (180+self.nacalox , 10+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (420+self.nacalox , 10+self.nacaloy ), (600+self.nacalox , 170+self.nacaloy ), 2)
            rect(screen, (0, 0, 0), (170+self.nacalox , 190+self.nacaloy , 280, 250), 2)
            #нарисовали крышу
            pygame.draw.line(screen,(0, 0, 0), (10+self.nacalox , 170+self.nacaloy ), (170+self.nacalox , 190+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (450+self.nacalox , 190), (600+self.nacalox , 170), 2)

            #рисум стропилы
            pygame.draw.line(screen,(0, 0, 0), (90+self.nacalox ,180+self.nacaloy ), (280+self.nacalox , 30+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (280+self.nacalox ,30+self.nacaloy ), (340+self.nacalox , 30+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (340+self.nacalox , 30), (520+self.nacalox , 180), 2)

            pygame.draw.line(screen,(0, 0, 0), (133+self.nacalox , 186+self.nacaloy ), (297+self.nacalox , 79+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (297+self.nacalox , 79+self.nacaloy ), (317+self.nacalox , 79+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (317+self.nacalox , 79+self.nacaloy ), (482+self.nacalox , 185+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (172+self.nacalox , 186+self.nacaloy ), (305+self.nacalox , 120+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (305+self.nacalox , 120+self.nacaloy ), (452+self.nacalox , 188 +self.nacaloy), 2)
            pygame.draw.line(screen,(0, 0, 0), (172+self.nacalox , 186+self.nacaloy ), (305+self.nacalox , 120+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (305+self.nacalox , 120+self.nacaloy ), (452+self.nacalox , 188+self.nacaloy ), 2)
            # нарисовали столпила

            # рисуем основыние теплици
            pygame.draw.line(screen,(0, 0, 0), (11+self.nacalox , 578+self.nacaloy ), (170+self.nacalox , 440+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (10+self.nacalox , 597+self.nacaloy ), (172+self.nacalox , 449+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (172+self.nacalox , 446+self.nacaloy ), (447+self.nacalox , 446+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (451+self.nacalox , 440+self.nacaloy ), (600+self.nacalox , 580+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (446+self.nacalox , 446), (603+self.nacalox , 600), 2)

            # рисуем окна на левой стороне
            pygame.draw.line(screen,(0, 0, 0), (18+self.nacalox , 555+self.nacaloy ), (18+self.nacalox , 189+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (18+self.nacalox , 189+self.nacaloy ), (71+self.nacalox , 194+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (71+self.nacalox , 194), (71+self.nacalox , 506), 2)
            pygame.draw.line(screen,(0, 0, 0), (71+self.nacalox , 506), (18+self.nacalox , 555), 2)

            # дверка в закрытом виде как окно 
            pygame.draw.line(screen,(0, 0, 0), (88+self.nacalox , 197+self.nacaloy ), (158+self.nacalox , 203+self.nacaloy ) , 2)
            pygame.draw.line(screen,(0, 0, 0), (158+self.nacalox , 203+self.nacaloy ), (159+self.nacalox , 435+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (159+self.nacalox , 435+self.nacaloy ), (92+self.nacalox , 489+self.nacaloy ) , 2)
            pygame.draw.line(screen,(0, 0, 0), (92+self.nacalox , 489+self.nacaloy ) ,  (88+self.nacalox , 197+self.nacaloy ), 2)

            # рисуем окно на правой стороне
            pygame.draw.line(screen,(0, 0, 0), (460+self.nacalox , 203+self.nacaloy ), (511+self.nacalox , 196+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (511+self.nacalox , 196+self.nacaloy ), (511+self.nacalox , 479+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (511+self.nacalox , 479+self.nacaloy ), (459+self.nacalox , 436+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (459+self.nacalox , 436), (460+self.nacalox , 203), 2)

            pygame.draw.line(screen,(0, 0, 0), (521+self.nacalox , 488+self.nacaloy ), (521+self.nacalox , 195+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (521+self.nacalox , 195+self.nacaloy ), (587+self.nacalox , 187+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (587+self.nacalox , 190+self.nacaloy ), (589+self.nacalox , 549+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (589+self.nacalox , 549 +self.nacaloy), (521+self.nacalox , 488+self.nacaloy ), 2)

            # рисуем окно на правой стороне
            rect(screen, (0, 0, 0), (203+self.nacalox , 237+self.nacaloy , 70, 60), 2)
            rect(screen, (0, 0, 0), (203+self.nacalox , 371+self.nacaloy , 70, 60), 2)
            # рисуем вентиляцию на крыне
            rect(screen, (0, 0, 0), (220 + self.nacalox, 460++self.nacaloy, 130, 40), 2)

            text444 = font.render("Закупорить", True, black, white)
            screen.blit(text444, [230 + self.nacalox, 470++self.nacaloy])

            pygame.draw.line(screen,(0, 0, 0), (310+self.nacalox , 86+self.nacaloy ), (400+self.nacalox , 139+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (400+self.nacalox , 139+self.nacaloy ), (372+self.nacalox , 146+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (372+self.nacalox , 146+self.nacaloy ), (313+self.nacalox , 118+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (313+self.nacalox , 118+self.nacaloy ), (310+self.nacalox , 86+self.nacaloy ), 2)

            #rect(screen, (0, 0, 0), (107+self.nacalox , 205+self.nacaloy , 49, 230)) открытая дверь
            #rect(screen, (0, 0, 0), (500+self.nacalox , 30+self.nacaloy , 80, 80),2)
            # pygame.draw.lines(Surface, color, closed, pointlist, width=1)
            #Нарисовать линию, соединяющую точки из последовательности pointlist на поверхности Surface,
            #цветом color, с толщиной линии width. Каждая точка представлена парой координат.
            #ЕслиScena параметр closed равен True, конечная точка соединяется с начальной.
            Scena.activmenu = "0"
            print ("главная"+Scena.activmenu)
            #Scena.sost()
        elif  name=="1":
            self.nacalox = x
            self.nacaloy = y
            rect(screen, (white), (10+self.nacalox, 10+self.nacaloy , 590, 590),)
            rect(screen, (0, 0, 0), (10+self.nacalox, 10+self.nacaloy , 590, 590),5)
            

            for i in signal.SIG:
                x1,y1,x2,y2=i
                pygame.draw.line(screen,(0, 0, 0), (x1+self.nacalox , y1+self.nacaloy ), (x2+self.nacalox , y2+self.nacaloy ), 2)


            
        elif  name=="2":
            self.nacalox = x
            self.nacaloy = y
            rect(screen, (white), (10+self.nacalox, 10+self.nacaloy , 590, 590),)
            rect(screen, (0, 0, 0), (10+self.nacalox, 10+self.nacaloy , 590, 590),5)
            
            for i in voda.SIG:
                x1,y1,x2,y2=i
                pygame.draw.line(screen,(0, 0, 0), (x1+self.nacalox , y1+self.nacaloy ), (x2+self.nacalox , y2+self.nacaloy ), 2)

            
        elif  name=="3":
            self.nacalox = x
            self.nacaloy = y
            rect(screen, (white), (10+self.nacalox, 10+self.nacaloy , 590, 590),)
            rect(screen, (0, 0, 0), (10+self.nacalox, 10+self.nacaloy , 590, 590),5)

            
            for i in came.SIG:
                x1,y1,x2,y2=i
                pygame.draw.line(screen,(0, 0, 0), (x1+self.nacalox , y1+self.nacaloy ), (x2+self.nacalox , y2+self.nacaloy ), 2)








        pygame.display.update()
       

       
        
    def sost(self):             #     пишем  текст в левом верхнем углу сцены состояние ардуины вызодим item(1-3)

        if self == tepl:
           
            tempin ="25"
        
            score = str(self. item1)+str(self. item2)+str(self.item3) 
            text = font.render("состояние ард. ",True,black ,white )
            screen.blit(text, [20+self.nacalox ,15])
            self.score=score
            text = font.render("My text",True,black)
            textе = font.render("ард. "+str(score),True, black, white )
            screen.blit(textе, [20+self.nacalox ,30])
            try:
                textе2 = font.render("температура " + tepl.tempin, True, black, white)
                screen.blit(textе2, [20 + self.nacalox, 50])
            except:
                print("ждем определения поля ")



            pygame.display.update()
        elif self ==signal:
            print ("tepl")
        elif self ==voda:
            print ("voda")
        elif self ==came:
            
            textе24 = font.render("нет камер",True, black, white )
            screen.blit(textе24, [20+Scena.nacalox ,30])
            pygame.display.update()
    def sevesost(self):
        if self == tepl:
            doorstr = "door "
            pechstr = "pech "
            fortstr = "fort "
            openstr = "open "
            closestr = "close "
            summasrt = ""
            summasrt=""
            if self. item1== 0:
                summasrt = summasrt + doorstr + closestr
                door = False
            else:
                summasrt = summasrt + doorstr + openstr
                door = True
            if self. item2 == 0:
                summasrt = summasrt + pechstr + closestr
                pech= False
            else:
                summasrt = summasrt + pechstr + openstr
                pech = True
            if self. item3 == 0:
                summasrt = summasrt + fortstr + closestr
                fort= False
            else:
                summasrt = summasrt + fortstr + openstr
                fort = True
            summasrt = summasrt +tepl.tempin
            print(summasrt)
            file1 = open('sostep.txt', 'w')
            file1.write(summasrt)
            file1.close()
            data = [door, pech, fort]
            with open('data.pickle', 'wb') as f:
                pickle.dump(data, f)

class Ports(Scena):
    def __init__(self,portcom1="COM3"):
        self.portcom1=portcom1
        self.good=1
        self.readport()

    def proverka(self):
        if self == teplp:
            try:
                ser = serial.Serial(self.portcom1, 9600, timeout=10)
                time.sleep(0.2)
                ser.close()
                self.good = 1
            except:
                print("неправильный сом порт состояния")
                self.good = 0
                comport.erreer()

    def readport(self): #  читаем из ардуино и выставляем item(1-3)j,j,обекта tepl
        if self.good==1:
            comreadnum =0
            while comreadnum <=10  : #начальное получение позиций
                print ("читаем sos")
                try:
                    ser = serial.Serial(self.portcom1, 9600, timeout=10)
                    ser.write(b'\x31') # так отправляем в сом порт ff
                    time.sleep(0.2)
                    comread  =ser.read(ser.inWaiting())# ser.readline() #reading up to 1 bytes
                    print (len(comread))
                    if (len(comread)) == 5:
                        comreadnum += 11
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
                        ser.close()

                except:
                    print ("неправильный сом порт состояния")
                    do1 = "1"
                    pec = "1"
                    foo = "1"
                    print(do1, pec, foo)
                    comport.erreer()
            comreadnum += 1
            #self. item1 = do1   # переменная двери
            #self. item2 = pec    # пременная окна печки
            #self. item3 = foo     # переменная форточки в крыше

            tepl.item1 = int(do1)   # переменная двери
            tepl.item2 = int(pec)   # пременная окна печки
            tepl.item3 = int(foo)   # пременная форточки
            print (tepl.item1,tepl.item2,tepl.item3)
        else:
            do1 = "1"
            pec = "1"
            foo = "1"
            tepl.item1 = int(do1)  # переменная двери
            tepl.item2 = int(pec)  # пременная окна печки
            tepl.item3 = int(foo)  # пременная форточки
            print(tepl.item1, tepl.item2, tepl.item3)
    def write_item(self,itemnum):

        if self == teplp:
            if self.good == 1:
                if itemnum==1:
                    print("дверь serial print")
                    if tepl.item1==1:
                        try:
                            ser = serial.Serial(self.portcom1, 9600, timeout=10)


                            ser.write(b'\x1a')  # так отправляем в сом порт 1а
                            time.sleep(0.2)
                            ser.close()
                            print("дверь x0a")

                        except:
                            print("неправильный сом порт")
                    if tepl.item1==0:
                        try:
                            ser = serial.Serial(self.portcom1, 9600, timeout=10)

                            ser.write(b'\x0a')  # так отправляем в сом порт 1а
                            time.sleep(0.2)
                            ser.close()
                            print("дверь x0a")
                        except:
                            print("неправильный сом порт")
                            comport.erreer()
                if itemnum == 2:
                    print("pech serial print")
                    if tepl.item2 == 1:
                        try:
                            ser = serial.Serial(self.portcom1, 9600, timeout=10)

                            ser.write(b'\x1b')  # так отправляем в сом порт 1а
                            time.sleep(0.2)
                            ser.close()
                            print("pech x0a")

                        except:
                            print("неправильный сом порт")
                            comport.erreer()
                    if tepl.item2 == 0:
                        try:
                            ser = serial.Serial(self.portcom1, 9600, timeout=10)

                            ser.write(b'\x0b')  # так отправляем в сом порт 1а
                            time.sleep(0.2)
                            ser.close()
                            print("pech x0a")
                        except:
                            print("неправильный сом порт")
                            comport.erreer()
                if itemnum == 3:
                    print("Форточка serial print")
                    if tepl.item3 == 1:
                        try:
                            ser = serial.Serial(self.portcom1, 9600, timeout=10)

                            ser.write(b'\x1c')  # так отправляем в сом порт 1а
                            time.sleep(0.2)
                            ser.close()
                            print("форточка x1с")
                            comport.erreer()

                        except:
                            print("неправильный сом порт")
                    if tepl.item3 == 0:
                        try:
                            ser = serial.Serial(self.portcom1, 9600, timeout=10)

                            ser.write(b'\x0c')  # так отправляем в сом порт 1а
                            time.sleep(0.2)
                            ser.close()
                            print("pech x0c")
                        except:
                            print("неправильный сом порт")
                            comport.erreer()
        elif self == signal:
            print("tepl")
        elif self == voda:
            print("voda")
        elif self == came:
            print("cam")
    def tempreadd(self):    #читаем температкру
        read1 = False
        print("читаем")
        if self == teplp:
            if self.good == 1:
                try:
                    ser = serial.Serial(self.portcom1, 9600, timeout=10)
                    ser.write(b'\x32')  # так отправляем в сом порт 32
                    time.sleep(0.2)
                    comread2 = ser.readline(ser.inWaiting())
                    time.sleep(0.2)
                    ser.close()
                    print(comread2)
                    print(len(comread2))
                    if (len(comread2)) == 4:
                        print(comread2[0])
                        print(comread2[1])
                        print(comread2[2])
                        print(comread2[3])
                        tepl.tempin = str(chr(comread2[0]) + chr(comread2[1]))



                except:
                    print("неправильный сом порт1")
                    comport.erreer()
        elif self == signal:
            print("signal")
    def tempstabrez(self):
        if self == teplp:
            if self.good == 1:
                try:
                    print("читаем sos1")
                    print("читаем темпер. стабилизациии режим.")
                    ser = serial.Serial(self.portcom1, 9600, timeout=10)
                    ser.write(b'\x01')  # так отправляем в сом порт 01
                    time.sleep(0.1)
                    stabtemprez = ser.readline(ser.inWaiting())  # reading up to 1 bytes
                    ser.close()
                    print(stabtemprez)
                    print(len(stabtemprez))
                    if (len(stabtemprez)) == 5:

                        print(stabtemprez[0])
                        print(stabtemprez[1])
                        print(stabtemprez[2])
                        print(stabtemprez[3])
                        print(stabtemprez[4])
                        tepl.stabtem = str(chr(stabtemprez[0]) + chr(stabtemprez[1]))
                        print("температура стабилизации" + tepl.stabtem)
                        tepl.rez = str(chr(stabtemprez[2]))
                        print("режим" + tepl.rez)
                except:
                    print("неправильный сом порт1")
                    comport.erreer()

        elif self == signal:
            print("signal")
    def set_tempstabrez(self):
        if self == teplp:
            if self.good == 1:
                print(int(tepl.xtemp))
                try:
                    ser = serial.Serial(self.portcom1, 9600, timeout=10)
                    if int(tepl.xtemp) == 15:
                        ser.write(b'\x34')  # так отправляем в сом порт ff
                    elif int(tepl.xtemp) == 16:
                        ser.write(b'\x35')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 17:
                        ser.write(b'\x36')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 18:
                        ser.write(b'\x37')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 19:
                        ser.write(b'\x38')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 20:
                        ser.write(b'\x39')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 21:
                        ser.write(b'\x3a')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 22:
                        ser.write(b'\x3b')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 23:
                        ser.write(b'\x3c')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 24:
                        ser.write(b'\x3d')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 25:
                        ser.write(b'\x3e')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 26:
                        ser.write(b'\x3f')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 27:
                        ser.write(b'\x40')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 28:
                        ser.write(b'\x41')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 29:
                        ser.write(b'\x42')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 30:
                        ser.write(b'\x43')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 31:
                        ser.write(b'\x44')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 32:
                        ser.write(b'\x45')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 33:
                        ser.write(b'\x46')  # так отправляем в сом порт ff
                    elif tepl.xtemp == 33:
                        ser.write(b'\x47')  # так отправляем в сом порт ff

                    time.sleep(0.2)
                    ser.close()
                except:
                    print("неправильный сом порт")
                    comport.erreer()
    def zakuporit(self):            #закупорить суда приходим из sobitie
        if self == teplp:
            if self.good == 1:
                try:
                    ser = serial.Serial(self.portcom1, 9600, timeout=10)
                    ser.write(b'\x02')  # так отправляем в сом порт 02
                    time.sleep(0.1)
                    ser.close()
                except:
                    print("неправильный сом порт")
                    comport.erreer()


class MenuScen(Scena):
    def __init__(self,x,txt,obj=0):
        self.dlina = 70 
        self.name = txt
        self.num =x
        rect(screen, (white), (19, 15+(self.dlina*self.num)  , 270, 60))
        rect(screen, (0, 0, 0), (21, 18+(self.dlina*self.num) , 267, 57),3)
        textе2 = font.render(txt ,True, black, white )
        screen.blit(textе2, [25 ,22+(self.dlina*self.num)])
        if obj==tepl:
            txt2=obj.itname1+" "+obj.itname2+" "+obj.itname3
            textе3 = font.render(txt2 ,True, black, white )
            screen.blit(textе3, [25 ,42+(self.dlina*self.num)]) 
        if obj==signal:
            txt2=obj.itname1+" "+obj.itname2+" "+obj.itname3
            textе3 = font.render(txt2 ,True, black, white )
            screen.blit(textе3, [25 ,42+(self.dlina*self.num)]) 
        if obj==voda:
            txt2=obj.itname1+" "+obj.itname2+" "+obj.itname3
            textе3 = font.render(txt2 ,True, black, white )
            screen.blit(textе3, [25 ,42+(self.dlina*self.num)]) 
        if obj==came:
            txt2=obj.itname1+" "+obj.itname2+" "+obj.itname3
            textе3 = font.render(txt2 ,True, black, white )
            screen.blit(textе3, [25 ,42+(self.dlina*self.num)]) 


        pygame.display.update()

    def arctivsc(self, curcsor):
        Scena.activmenu1 =Scena.activmenu
        Scena.activmenu = curcsor 
        print ("main-sc old"+Scena.activmenu1)
        print ("main-sc"+Scena.activmenu)
        rect(screen, (white), (19, 15+(self.dlina*int(Scena.activmenu1))  , 270, 63),3)
        rect(screen, (0, 0, 0), (19, 15+(self.dlina* int(Scena.activmenu)) , 270, 63),3)
        pygame.display.update()

    def sostoynmen(self):
        textе412 = font.render(tepl.score+"  "+tepl.tempin,True, black, white )
        screen.blit(textе412, [200 ,20+(self.dlina*self.num)])


        
class Runs(Scena):
    def __init__(self):
        try:
            file1 = open('config.txt', 'r')
            self.line = file1.readline()

            file1.close
            textе402 = font.render("прочитана", True, black, white)  # =portcom1
            screen.blit(textе402, [670, 655])

        except:
            textе402 = font.render("нет файла", True, black, white)  # =portcom1
            screen.blit(textе402, [670, 655])
            self.line = "COM3"

        self.i = 2
    def ranportstart(self):
        rect(screen, (0, 0, 0), (306, 607, 590, 90),6 )
        textе400 = font.render("Теплица                   Сигн--ция                 Вода  ", True, black, white)
        screen.blit(textе400, [310, 610])
        try:
            textе401 = font.render(str(teplp.portcom1), True, black, white)       #=portcom1
            screen.blit(textе401, [410, 610])
        except:
            textе401 = font.render("COM3", True, black, white)               # =portcom1
            screen.blit(textе401, [410, 610])

    def sobitieport(self):
        self.Com=["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM7","COM8","COM9","COM11`","COM12","COM12"
             ,"COM13","COM14","COM15","COM16","COM18","COM19","COM20","COM21","COM22","COM23","COM24"
             ,"COM25","COM26","COM27","COM28","COM29","COM30","Demo","file  "]

        if Scena.x1 >= 368 and Scena.x1 <= 400 and Scena.y1 >= 640 and Scena.y1 <= 660:
            if self.i>0:
                self.i-=1
        if Scena.x1 >= 470 and Scena.x1 <= 500 and Scena.y1 >= 640 and Scena.y1 <= 660:
            if self.i<=len(self.Com) - 2:
                self.i+=1


        textе401 = font.render("<<  "+self.Com[self.i]+"  >>    Установить     Записать ", True, black, white)  # =portcom1
        screen.blit(textе401, [370, 635])

        if Scena.x1 >= 520 and Scena.x1 <= 640 and Scena.y1 >= 640 and Scena.y1 <= 660:
            teplp.portcom1 = self.Com[self.i]
            self.ranportstart()
            teplp.proverka()
            textе401 = font.render("                                                  ", True, black, white)  # =portcom1
            screen.blit(textе401, [370, 635])
            if teplp.good == 1:
                textе402 = font.render("     правильный ком порит             ", True, black, white)  # =portcom1
                screen.blit(textе402, [370, 635])
        if Scena.x1 >= 673 and Scena.x1 <= 761 and Scena.y1 >= 640 and Scena.y1 <= 660:

            summasrt=teplp.portcom1
            file1 = open('config.txt', 'w')
            file1.write(summasrt)
            file1.close()
            textе401 = font.render("                                                  ", True, black, white)  # =portcom1
            screen.blit(textе401, [370, 635])

            textе402 = font.render("записано", True, black, white)  # =portcom1
            screen.blit(textе402, [670, 655])

    def erreer(self):
        textе403 = font.render(" неправильныйй сом порт ", True, black, white)  # =portcom1
        screen.blit(textе403, [370, 655])
        self.good = 0






FPS = 50
screen = pygame.display.set_mode((910, 710))
pygame.display.set_caption("Tepliche")
rect(screen, (255, 255, 255), (6, 6 , 896, 696),)
done=False
curcsor="nezn"



font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
finished = False
comport = Runs()
comport.ranportstart()

A=[(10,253,289,16),(289,16,593,253),(593,253,10,253),(67,253,67,595),(552,595,553,253),(98,596,98,318),(98,318,177,318),(177,318,177,596),
   (226,316,226,448),(226,448,316,448),(318,448,318,316),(318,316,226,316),(405,596,405,315),(405,315,527,315),(527,315,527,596)]
B=[(8,312,454,312),(8,322,242,322),(239,322,239,438),(249,322,249,438),(249,322,405,322),(249,312,400,312),
   (404,324,404,438),(414,324,414,438),(414,322,454,322),(380,438,434,438),(380,498,434,498),(380,498,434,498)
  ,(434,498,434,438),(380,498,380,438),(216,498,270,498),(216 ,438,270,438),(216 ,438,216,498),(270 ,438,270,498) ]
C=[(10,300,590,300),(300,10,300,590)]

activ= Scena(295,2,itname1="Дверь",itname2="ПечнаяДв",itname3="Окошко",name="1",rend=0 )

tepl = Scena(295,2,itname1="Дверь",itname2="Печка",itname3="Форточка",name="0",rend=1 )

signal=Scena(295,2,itname1="Дверь",itname2="ПечнаяДв",itname3="Окошко",name="1",rend=0 ) 
signal.SIG=A
voda=Scena(295,2,itname1="вод-од",itname2="бочк.теп",itname3="бочк.дом",name="2",rend=0 )
voda.SIG=B
came=Scena(295,2,itname1="Камера1",itname2="Камера2",itname3="Кемера3",name="3",rend=0 )
came.SIG=C
tepl1 = MenuScen(0,"Теплица",obj=tepl)
tepl2 = MenuScen(1,"охрана",obj=signal)
tepl3 = MenuScen(2,"Вода",obj=voda)
tepl4 = MenuScen(3,"Камеры",obj=came )
tepl.sost()
tepl1.arctivsc("0")
teplp = Ports(portcom1=comport.line)      #self.line
tepl.xtemp=20
sobitie=0
timer1=0
while not finished:
    clock.tick(FPS)
    if curcsor=="nizniy":
        comport.sobitieport()
        curcsor == "nezn"
        Scena.x1 = 0  # сбрасываем координаты собитий от предидущего цикла
        Scena.y1 = 0





    if timer1 == 60:
        timer1 = 0
    timer1 += 1
    textе33 = font.render(str(timer1), True, black, white)
    screen.blit(textе33, [10, 500])
    print(timer1)
    Scena.pererisovka()
    if int(Scena.activmenu) ==0:           #выбор действия в зависимости от конкретной сцены и прописываем необходимые действия если сцена не выбраеа

        if timer1 == 1:
            teplp.tempstabrez()
            teplp.tempreadd()
        if timer1 == 3:
            tepl.sost()
            tepl.sowsust()
            tepl.drawtempset()
            tepl.prrintstabterm()
        if sobitie==1:
            sobitie==0

            tepl.sobitiescen()
        if timer1 == 2:
            teplp.readport()
            tepl.sevesost()
    else:
        if timer1 == 2:
            teplp.readport()
            tepl.sevesost()
            teplp.tempreadd()
            tepl1.sostoynmen()
         #print (tepl.settempstab())
    if int (Scena.activmenu) ==1:
        textе33 = font.render(Scena.activmenu ,True, black, white )
        screen.blit(textе33, [10 ,500])
    elif int(Scena.activmenu) ==2:
        textе33 = font.render(Scena.activmenu ,True, black, white )
        screen.blit(textе33, [10 ,500])
    elif int(Scena.activmenu) ==3:
        textе33 = font.render(Scena.activmenu ,True, black, white )
        screen.blit(textе33, [10 ,500])
        came.sost()
    pygame.display.update()

    
    #tepl.sowsust()
    #Scena.sost(tepl)
    Scena.x1 = 0    # сбрасываем координаты собитий от предидущего цикла
    Scena.y1 = 0
    for event in pygame.event.get():    #обрабатываем кобытие назатия мыши
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
               x1,y1 = event.pos
               Scena.x1=x1
               Scena.y1=y1
               print (Scena.x1)
               textе36 = font.render(str(Scena.x1)+" "+str(Scena.y1) ,True, black, white )
               screen.blit(textе36, [10 ,550])
               print(int(Scena.x1))
               
               pygame.display.update()

               print (x1-300,y1 )
            elif event.button == 1:
                x,y = event.pos
                curcsor = cursor(x,y)
                Scena.x1=x
                Scena.y1=y
                print (curcsor)
                if curcsor=="nezn":
                    print (curcsor)
                if curcsor=="scena":
                    curcsor="nezn"
                    sobitie=1     
                elif curcsor=="0" :
                    tepl1.arctivsc(curcsor)
                elif curcsor=="1":
                    tepl1.arctivsc(curcsor)
                elif curcsor=="2":
                    tepl1.arctivsc(curcsor)
                elif curcsor=="3":
                    tepl1.arctivsc(curcsor)
                            


                else:
                   print (curcsor) 





pygame.quit()                
