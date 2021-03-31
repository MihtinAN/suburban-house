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

def cursor(x,y):
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

    return "nezn" 




class Scena:
    #зисуем сцену
    def __init__(self,x,y,itname1=" ",itname2=" ",itname3=" ",name=" ",rend=0 ):
        self. door = 0    # переменная двери
        self. pech = 0     # пременная окна печки
        self. fort = 0      # переменная форточки в крыше
        self.itname1=itname1
        self.itname2=itname2
        self.itname3=itname3
        if rend==1: 
            self.drawscene(x,y,name)
            self.name=name
            print(self)
    def pererisovka():
       if Scena.activmenu1 != Scena.activmenu:
           print("перерисовка"+Scena.activmenu1+"  "+Scena.activmenu)
           Scena.activmenu1 = Scena.activmenu
           Scena.drawscene(activ,295,2,Scena.activmenu)
    def drawscene(self,x,y,name,):
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

            pygame.draw.line(screen,(0, 0, 0), (310+self.nacalox , 86+self.nacaloy ), (400+self.nacalox , 139+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (400+self.nacalox , 139+self.nacaloy ), (372+self.nacalox , 146+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (372+self.nacalox , 146+self.nacaloy ), (313+self.nacalox , 118+self.nacaloy ), 2)
            pygame.draw.line(screen,(0, 0, 0), (313+self.nacalox , 118+self.nacaloy ), (310+self.nacalox , 86+self.nacaloy ), 2)

            #rect(screen, (0, 0, 0), (107+self.nacalox , 205+self.nacaloy , 49, 230)) открытая дверь
            rect(screen, (0, 0, 0), (500+self.nacalox , 30+self.nacaloy , 80, 80),2)
            # pygame.draw.lines(Surface, color, closed, pointlist, width=1)
            #Нарисовать линию, соединяющую точки из последовательности pointlist на поверхности Surface,
            #цветом color, с толщиной линии width. Каждая точка представлена парой координат.
            #ЕслиScena параметр closed равен True, конечная точка соединяется с начальной.
            Scena.activmenu = "0"
            print ("главная"+Scena.activmenu)
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
        
        
        
    def sost(self):
        # text = font.render("My text",True,black)
        print ("sost")
        tempin ="25"
        
        score = str(self. door)+str(self. pech)+str(self. fort) 
        text = font.render("состояние ард. ",True,black ,white )
        screen.blit(text, [20+self.nacalox ,15])
    
        text = font.render("My text",True,black)
        textе = font.render(" ард. "+str(score),True, black, white )
        screen.blit(textе, [20+self.nacalox ,30])
        textе2 = font.render("температура "+tempin,True, black, white )
        screen.blit(textе2, [20+self.nacalox ,50])
        pygame.display.update()    

class Ports(Scena):
    pass
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


        
class Runs:
    def ran1(self):
        pass



FPS = 5
screen = pygame.display.set_mode((910, 710))
pygame.display.set_caption("Tepliche")
rect(screen, (255, 255, 255), (6, 6 , 896, 696),)
done=False


fontObj = pygame.font.Font('freesansbold.ttf', 50)
textSurfaceObj = fontObj.render('Hello world!', True, yellow, blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (500, 400)
pygame.display.flip()
font = pygame.font.Font(None, 30)
    
   

clock = pygame.time.Clock()
finished = False

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
while not finished:
    clock.tick(FPS)
    Scena.pererisovka()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
               x1,y1 = event.pos 

               print (x1-300,y1 )
            elif event.button == 1:
                x,y = event.pos
                curcsor = cursor(x,y)
                print (curcsor)
                if curcsor=="nezn":
                    print (curcsor)
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
