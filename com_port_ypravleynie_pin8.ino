
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
// пин подключения контакта OUT
#define PIN_OUT A0
LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
int pinLED2 = 13;
int pinLED3 = 3;
int pinLED4 = 4;



void setup() {
Serial.begin(9600);
lcd.init();                      // Инициализация lcd    
lcd.backlight();                 // Включаем подсветку
lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
lcd.print("figura maid");   // Выводим текст

// Инициализируем цифровой вход/выход в режиме выхода.
  pinMode(LED_BUILTIN, OUTPUT);   
  pinMode(pinLED3, OUTPUT);   
  pinMode(pinLED4, OUTPUT);   
  pinMode(5, INPUT);   // назначить выводу пот ввода ( )
  digitalWrite(5, HIGH);  // включить подтягивающий резистор
  pinMode(6, INPUT);   // назначить выводу пот ввода ( )
  digitalWrite(6, HIGH);  // включить подтягивающий резистор
  pinMode(7, INPUT);   // назначить выводу пот ввода ( )
  digitalWrite(7, HIGH);  // включить подтягивающий резистор


delay(1000);  




int temp=40;
int ttemp=1000;

lcd.setCursor(14,1);       
       lcd.print(temp);
delay(500);
 lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  lcd.print("mod teplicha t");
  lcd.setCursor(14,1); 
  lcd.print(temp);  // Выводим текст
}

void loop() {
String  data="";
int temp=40;
int x=0;
int ttemp=1000; 
int x1=1; 
int dver = 0;
int pech = 0;
int fort = 0;
 while (x1 == 1) {
  ttemp = analogRead(A0);
  lcd.setCursor(12,0);
  lcd.print(ttemp); 
  
  if (Serial.available() > 0) {
  x = Serial.read();
  Serial.println(x);
                // Включаем подсветку
  lcd.setCursor(0,0);              // Устанавливаем курсор в начало 1 строки
  lcd.print(x);
  lcd.setCursor(0,0); 
  
  lcd.setCursor(0,1);              // Устанавливаем курсор в начало 2 строки
  lcd.print("mod teplicha t");
  lcd.setCursor(14,1); 
  lcd.print(temp);  // Выводим текст
  

  if (x == 26) {
       lcd.setCursor(5,0); 
       lcd.print(1);
       digitalWrite(LED_BUILTIN, HIGH);
       dver = 1;
       }
  if (x == 10) {
       lcd.setCursor(5,0); 
       lcd.print(0);
       digitalWrite(LED_BUILTIN, LOW); 
       dver = 0;
       }
   if (x == 27) {
       lcd.setCursor(6,0); 
       lcd.print(1);
       pech = 1;
       }
   if (x == 11) {
       lcd.setCursor(6,0); 
       lcd.print(0);
       pech = 0;
       }
   if (x == 28) {
       lcd.setCursor(7,0); 
       lcd.print(1);
       fort = 1;
       }
   if (x == 12) {
       lcd.setCursor(7,0); 
       lcd.print(0);
       fort = 0;
       }
   if (x == 49) {
       lcd.setCursor(9,0); 
       lcd.print(1);
       data=String(dver)+String(pech)+String(fort);
       
       Serial.println(data);
       }
   if (x == 50) {
       lcd.setCursor(9,0); 
       lcd.print(0);
       Serial.write("22");
       }
   
   if (x >= 70 and x<80) {
        temp=x;
       lcd.setCursor(10,0);       
       lcd.print(temp);
       }


 }

  }

}
