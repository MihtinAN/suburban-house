
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup()
{
  lcd.init();                      // initialize the lcd 
  lcd.backlight();
  Serial.begin(9600);



const int BUTTON9=9; // Контакт 2 для подключения кнопки дверь звонить 
const int BUTTON8=8; // Контакт 3 для подключения кнопки напряжение
const int BUTTON7=7; // Контакт 4 для подключения кнопки замок навесной













}
void loop(){

 
 
 
 
 pinMode (9, INPUT_PULLUP);
 pinMode (8, INPUT_PULLUP);
 pinMode (7, INPUT_PULLUP);
 pinMode (6, OUTPUT);
 pinMode (5, OUTPUT);
 pinMode (4, OUTPUT);


Serial.begin(9600);
lcd.init();                      // Инициализация lcd    
lcd.backlight();                 // Включаем подсветку
lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
lcd.print("figura maid");        // Выводим текст
delay(1000);  



int temp=40;

int ttemp=1000;

lcd.setCursor(14,1);       
lcd.print(temp);
delay(500);
 lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  lcd.print("mod teplichat");
  lcd.setCursor(14,1); 
  lcd.print(temp);  // Выводим текст




  
int BUTTON9=9; // Контакт 2 для подключения кнопки дверь звонить 
int BUTTON8=8; // Контакт 3 для подключения кнопки напряжение
int BUTTON7=7; // Контакт 4 для подключения кнопки замок навесной
int BUTTON6=6; // Контакт 2 для подключения кнопки дверь звонить 
int BUTTON5=5; // Контакт 3 для подключения кнопки напряжение
int BUTTON4=4; // Контакт 4 для подключения кнопки замок навесной}
 
 
int tekButton9 = HIGH;
int tekButton8 = HIGH;
int tekButton7 = HIGH;

int timer=0;
String  data="";
String  datat="";
int temp1;

int x=0;
int deyst1=0;
int deyst2=0;
int deyst3=0;


int i=1; 
int dver1 = 0;
int pech1 = 0;
int fort1 = 0;
int dver2 = 0;
int pech2 = 0;
int fort2 = 0;


int dver = 0;
int pech = 0;
int fort = 0;
  while (i==1) 
  {
  ttemp = analogRead(A0);
  //lcd.setCursor(11,0);
  //lcd.print(ttemp); 
  temp1=((710-ttemp)/8)-1;
  lcd.setCursor(14,0);
  lcd.print(int(temp1));
  timer=timer+1;
  if (timer <=100){
  lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  lcd.print("-mod teplichat");        // Выводим текст
  }
  if (timer >=100){
   lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  lcd.print("mod teplicht- ");        // Выводим текст
  }
  if (timer >=200){
  timer =0;
  }
  tekButton9=digitalRead(9);
  if (tekButton9==0 && dver1 == 0 ){
    dver2 = 1;
    deyst1=1;
    delay(200);
  }
  if (tekButton9==0 && dver1 == 1 ){
    dver2 = 0;
    deyst1=1;
    delay(200);
  }
  dver1 = dver2;
  tekButton7=digitalRead(7);  
  if (tekButton7==0 && pech1 == 0 ){
    pech2 = 1;
    deyst2=1;
    delay(200);
  }
  if (tekButton7==0 && pech1 == 1 ){
    pech2 = 0;
    deyst2=1;
    delay(200);
  }
  pech1 = pech2;
 tekButton8=digitalRead(8);
if (tekButton8==0 && fort1 == 0 ){
    fort2 = 1;
    deyst3=1;
    delay(200);
  }
  if (tekButton8==0 && fort1 == 1 ){
    fort2 = 0;
    deyst3=1;
    delay(200);
  }
  fort1 = fort2;
 
  
  
  lcd.setCursor(0,0); 
  lcd.print(tekButton9);
  lcd.setCursor(1,0); 
  lcd.print(tekButton8);
  lcd.setCursor(2,0); 
  lcd.print(tekButton7);
 lcd.setCursor(4,0); 
  lcd.print(dver1);
  lcd.setCursor(5,0); 
  lcd.print(pech1);
  lcd.setCursor(6,0); 
  lcd.print(fort1);
 if (deyst1 == 1){
    dver = dver1;
    digitalWrite(BUTTON6,dver1);
    deyst1 =0;
 }
   if (deyst2 == 1){
    pech = pech1;
    digitalWrite(BUTTON5,pech1);
    deyst2 = 0;
 }
   if (deyst3 == 1){
    fort = fort1;
    digitalWrite(BUTTON4,fort1);
    deyst3 = 0;
 }
   
   
   
   
   if (Serial.available() > 0) {
  x = Serial.read();
  //Serial.println(x);                Включаем подсветку
  lcd.setCursor(0,0);              // Устанавливаем курсор в начало 1 строки
 // lcd.print(x);
  lcd.setCursor(0,0); 
  
  lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  lcd.print("mod teplicha t");
  lcd.setCursor(14,1); 
  lcd.print(temp);  // Выводим текст
   if (x == 26  ) {                  // Устанавливаем дверь
       lcd.setCursor(8,0); 
       lcd.print(1);
       digitalWrite(BUTTON6, HIGH);
       dver = 1;
       dver1 = 1;
       lcd.setCursor(4,0); 
        lcd.print(dver1);
       }
   if (x == 10)   {
       lcd.setCursor(8,0); 
       lcd.print(0);
       digitalWrite(BUTTON6, LOW); 
       dver = 0;
       dver1 = 0;
      lcd.setCursor(4,0); 
       lcd.print(dver1);
       }//-------------------------------------------------------------------------------
   if (x == 27  )  {                    // Устанавливаем печ
       lcd.setCursor(9,0); 
       lcd.print(1);
       pech = 1;
       pech1 = 1;
       digitalWrite(BUTTON5, HIGH); 
        lcd.setCursor(5,0); 
        lcd.print(pech1);
       }
   if (x == 11  ) {
       lcd.setCursor(9,0); 
       lcd.print(0);
       pech = 0;
       pech1 = 0;
       digitalWrite(BUTTON5, LOW); 
        lcd.setCursor(5,0); 
       lcd.print(pech1);
       }//--------------------------------------------------------------------------------
   if (x == 28  ) {                   // Устанавливаем печ
       lcd.setCursor(10,0); 
      lcd.print(1);
       fort = 1;
       fort1 = 1;
        
       digitalWrite(BUTTON4, HIGH);
       lcd.setCursor(6,0); 
       lcd.print(fort1);// Устанавливаем форточка таботает горит
       }
   if (x == 12) {
       lcd.setCursor(10,0); 
       lcd.print(0);
       fort = 0;
       fort1 = 0;
       
       digitalWrite(BUTTON4, LOW); // Устанавливаем форточка таботает горит
        lcd.setCursor(6,0); 
        lcd.print(fort1);
       
       }
   if (x == 49) {
      
       data=String(dver)+String(pech)+String(fort);

       Serial.println(data);
        lcd.setCursor(8,0); 
       lcd.print(dver);
        lcd.setCursor(9,0); 
       lcd.print(pech);
       lcd.setCursor(10,0);
       lcd.print(fort);
       }
   if (x == 50) {
       
       datat=String(temp1);
       Serial.println(datat);
       
       
       }
   
   if (x >= 70 and x<100) {
       temp=x;
       lcd.setCursor(10,0);       
       lcd.print(temp);
       }
  }
 }
 

 
  
  
  
 

}
