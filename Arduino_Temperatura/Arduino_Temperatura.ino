//declaro variable para guardar temp en celsius
float tempC ;
//declaro varible para el pin A0
int pinSensorT = 0 ;
int ledRojo = 4;
int ledAma= 13;
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
  pinMode(ledRojo,OUTPUT);
  pinMode(ledAma,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
   //LEE LA TEMPERATURA
  tempC = analogRead(pinSensorT) ;
  tempC = (5.0 * tempC * 100)/1024.0 ;
  Serial.println(tempC);
  delay(2000);
  
  if(tempC >= 30){
    digitalWrite(ledRojo,HIGH);
  }else{
    if(tempC < 30){
      digitalWrite(ledRojo,LOW);
    }  
  }
   if(tempC <= 30){
    digitalWrite(ledAma,HIGH);
  }else{
    if(tempC > 30){
      digitalWrite(ledAma,LOW);
    }  
  }
}
