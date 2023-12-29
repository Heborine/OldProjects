int counter = 0;
long last_micros = 0;
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
void setup() 

{
  // put your setup code here, to run once:
Serial.begin(9600);
attachInterrupt(0, checker, RISING);
attachInterrupt(1, subtracter, RISING);
lcd.init();
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(7, OUTPUT);
}

void loop() {
  Serial.print("Cookies_Clicked:");
  Serial.println(counter);
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Cookie Clicker:") ;
  lcd.setCursor(1,1);
  lcd.print(counter);
  lcd.print("___()O0O");
 
 if (counter == 0){
 digitalWrite(9, LOW);
 digitalWrite(8, HIGH);
 digitalWrite(10, LOW);
 digitalWrite(7, LOW);
 digitalWrite(11, LOW);
digitalWrite(12, LOW);
 
 }
else if (counter == 1){
digitalWrite(9, HIGH);
digitalWrite(8, LOW);
digitalWrite(10, LOW);
digitalWrite(11, LOW);
digitalWrite(12, LOW);
digitalWrite(7, LOW);
}
else if (counter == -1){
digitalWrite(9, LOW);
digitalWrite(8, LOW);
digitalWrite(10, HIGH);
digitalWrite(11, LOW);
digitalWrite(12, LOW);
digitalWrite(7, LOW);
}
else if (counter == -4|counter < -4){
digitalWrite(9, LOW);
digitalWrite(8, LOW);
digitalWrite(10, LOW);
digitalWrite(11, HIGH);
digitalWrite(12, LOW);
digitalWrite(7, LOW);
}
else if (counter == 4|counter > 4){
digitalWrite(9, LOW);
digitalWrite(8, LOW);
digitalWrite(10, LOW);
digitalWrite(11, LOW);
digitalWrite(12, HIGH);
digitalWrite(7, LOW);
}
else if (counter == 2){
digitalWrite(9, LOW);
digitalWrite(8, LOW);
digitalWrite(10, LOW);
digitalWrite(11, LOW);
digitalWrite(12, LOW);
digitalWrite(7, HIGH);
}
 
}
 void checker()
 {
  // put your main code here, to run repeatedly:
if ((micros() - last_micros) >= 250000)
{
  counter = counter + 1;
  last_micros = micros ();
}
//if{
//counter = 1;
//}
}
void subtracter(){
  if ((micros() - last_micros) >= 250000)
{
  counter = counter - 1;
  last_micros = micros\
  ();
}
}


//if (counter = 1){
  
//}
//}
  
//}
//}
