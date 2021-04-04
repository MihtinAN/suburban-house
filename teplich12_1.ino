
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
 pinMode (10, INPUT_PULLUP);
pinMode (11, INPUT_PULLUP);
pinMode (12, INPUT_PULLUP);
pinMode (13, OUTPUT);

Serial.begin(9600);
lcd.init();                      // Инициализация lcd    
lcd.backlight();                 // Включаем подсветку
lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
lcd.print("figura maid");        // Выводим текст
delay(1000);  
int temp=30;
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
int tekButton11 = HIGH;
int tekButton10 = HIGH;
int tekButton12 = HIGH;
int timer2=0;
int timer1=0;
int timer=0;
String  datats="";
String  data="";
String  datat="";
int temp1;
int temp2;
int temp3;
int x=0;
int deyst1=0;
int deyst2=0;
int deyst3=0;
int stabyltem=0;
int stabyltem1=0;
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
  if (timer1 > 0){
    timer1=timer1+1;
    if (timer1==500){
      timer1=0;
    }
   }

   if (timer2 > 0){
    timer2=timer2+1;
    if (timer2==500){
      timer2=0;
    }
   }
  if (timer ==10){
  ttemp = analogRead(A0);           //читаем температуру
  //lcd.setCursor(11,0);
  //lcd.print(ttemp); 
  temp1=((710-ttemp)/8)-1;
  lcd.setCursor(14,0);
  lcd.print(int(temp1));
  }
  timer=timer+1;
  
  if (timer <=10){
  digitalWrite(13, LOW);
  lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  //lcd.print("-mod teplichat");        // Выводим текст
  }
  if (timer >=10){
  digitalWrite(13, HIGH);
  
  // lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  //lcd.print("mod teplicht- ");        // Выводим текст
  }
  if (timer >=20){
  timer =0;
  }
tekButton10=digitalRead(10);          //проверяем кнопку уменьшения тампературы

  //lcd.setCursor(0,1);
  //lcd.print(tekButton10); 
if (tekButton10==0  ){
  if (temp<=34){
  temp=temp+1;
  delay(300);
  }
}
 tekButton12=digitalRead(12);           // проверяем кнопкуувеличение температуры
  //lcd.setCursor(1,1);
  //lcd.print(tekButton12); 
if (tekButton12==0  ){
  if (temp>=15){
  temp=temp-1;
  delay(300);
  }
}
  if (tekButton11==0){
  lcd.setCursor(0,0); 
  lcd.print("R");
  delay(500);
  }
  if (tekButton9==0){
  lcd.setCursor(0,0); 
  lcd.print("D");
  delay(500);
  }
   if (tekButton8==0){
  lcd.setCursor(0,0); 
  lcd.print("F");
  delay(500);
  }
  if (tekButton7==0){
  lcd.setCursor(0,0); 
  lcd.print("P");
  delay(500);
  }
  if (tekButton10==0){
  lcd.setCursor(0,0); 
  lcd.print("+");
  delay(500);
  }      
  if (tekButton12==0){
  lcd.setCursor(0,0); 
  lcd.print("-");
  delay(500);
  }      
  
  //-------------------------------------------
  tekButton9=digitalRead(9);            //читаем кнопку тритера двери
  if (tekButton9==0 && dver1 == 0 ){
    dver2 = 1;
    deyst1=1;
    stabyltem=0;
    delay(600);
  }
  if (tekButton9==0 && dver1 == 1 ){
    dver2 = 0;
    deyst1=1;
    
    delay(600);
  }
  dver1 = dver2;
  tekButton7=digitalRead(7);            //читаем кнопку тритера печки
  if (tekButton7==0 && pech1 == 0 ){
    pech2 = 1;
    deyst2=1;
    
    delay(600);
  }
  if (tekButton7==0 && pech1 == 1 ){
    pech2 = 0;
    deyst2=1;
    
    delay(600);
  }
  pech1 = pech2;
 tekButton8=digitalRead(8);             //читаем кнопку тритера форточки
if (tekButton8==0 && fort1 == 0 ){
    fort2 = 1;
    deyst3=1;
    delay(600);
  }
  if (tekButton8==0 && fort1 == 1 ){
    fort2 = 0;
    deyst3=1;  
   delay(600);
  }
  fort1 = fort2;
  tekButton11=digitalRead(11);                //-------------------------------------------
if (tekButton11==0 && stabyltem1 == 1 ){      //читаем кнопку тритера режима стабилизации температуры
    stabyltem = 0;
    delay(500);
  }
  if (tekButton11==0 && stabyltem1 == 0 ){
    stabyltem = 1;
    delay(500);
  }
  stabyltem1 = stabyltem;
 
   lcd.setCursor(14,1);       
   lcd.print(temp);
  
  lcd.setCursor(11,0); 
  lcd.print(stabyltem1);
  
  lcd.setCursor(1,0); 
  lcd.print("D");
 
 lcd.setCursor(2,0); 
  lcd.print(dver1);
lcd.setCursor(3,0); 
  lcd.print("P");
  
  lcd.setCursor(4,0); 
  lcd.print(pech1);
  lcd.setCursor(5,0); 
  lcd.print("F");
  
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
  if (tekButton11==1){
  lcd.setCursor(0,0); 
  lcd.print("_");
  }
   if (tekButton9==1){
  lcd.setCursor(0,0); 
  lcd.print("_");
  }
   if (tekButton8==1){
  lcd.setCursor(0,0); 
  lcd.print("_");
  }
  if (tekButton7==1){
  lcd.setCursor(0,0); 
  lcd.print("_");
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
      digitalWrite(BUTTON6, HIGH);
       stabyltem=0;
       dver = 1;
       dver1 = 1;
       lcd.setCursor(4,0); 
        lcd.print(dver1);
       }
   if (x == 10)   {
       digitalWrite(BUTTON6, LOW);
       
       dver = 0;
       dver1 = 0;
      lcd.setCursor(4,0); 
       lcd.print(dver1);
       }//-------------------------------------------------------------------------------
   if (x == 27  )  {                    // Устанавливаем печ
       pech = 1;
       pech1 = 1;
        lcd.setCursor(5,0); 
        lcd.print(pech1);
       }
   if (x == 11  ) {
       pech = 0;
       pech1 = 0;
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
       if (x == 1) {
       datats=String(temp)+String(stabyltem1);
       Serial.println(datats);
       }
       if (x == 2) {
        fort = 0;
        dver = 0;
        stabyltem=0;
        pech = 0;
        }
        }
   if (x >= 51 and x<71) {
       temp=x-51+14;
       lcd.setCursor(14,1);       
       lcd.print(temp);
        stabyltem1=1;
        stabyltem=1;
      // Serial.println(temp);
       }
  temp2 = temp+3;  
 if (stabyltem1==1){
     
   
    
    
    lcd.setCursor(0,1);       
    lcd.print("stab  temp  ");
    //lcd.setCursor(6,1);       
    //lcd.print(temp+3);
      if (timer2 ==0){
       if (temp1 < temp){
       fort = 0;
       }
      if (temp1>=temp){
       
       fort = 1;
       fort1 = 1;
       timer2=1;
     }
      //lcd.setCursor(3,1);       
      // lcd.print(temp);
     }
 if (timer1 ==0){
 if  (temp1 < temp2){
  dver = 0;
 }
 if (temp1>= temp2){
   
       dver = 1;             
      dver1 = 1;
      timer1 = 1;
   }
    
       }
      lcd.setCursor(10,1);       
      lcd.print(timer1);
      if (timer2 ==0){
      lcd.setCursor(10,1);       
      lcd.print("0  ");  
      }
        lcd.setCursor(8,0); 
       lcd.print(dver);
       digitalWrite(BUTTON6, dver);

       lcd.setCursor(9,0); 
       lcd.print(pech);
       digitalWrite(BUTTON5,pech); 

       lcd.setCursor(10,0); 
       lcd.print(fort);
       digitalWrite(BUTTON4,fort);
      if (stabyltem==0){
      lcd.setCursor(0,1);       
       lcd.print("puchnoe ypr  ");
 }
 }
   if (stabyltem==0){
      lcd.setCursor(0,1);       
       lcd.print("puchnoe ypr  ");
 }  
 } 
}
  
