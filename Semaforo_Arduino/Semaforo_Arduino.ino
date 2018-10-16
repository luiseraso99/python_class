int ledRojo = 2;
int ledAmarillo = 4;
int ledVerde = 7;
int motor = 13;
void setup() {
  // put your setup code here, to run once:
 pinMode(ledRojo,OUTPUT);
 pinMode(ledAmarillo,OUTPUT);
 pinMode(ledVerde,OUTPUT);
 pinMode(motor,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledRojo,HIGH);
  delay(100);//tiempo de espera
  digitalWrite(ledRojo,LOW);
  delay(100);
    digitalWrite(ledAmarillo,HIGH);
  delay(150);//tiempo de espera
  digitalWrite(ledAmarillo,LOW);
  delay(150);
    digitalWrite(ledVerde,HIGH);
  delay(150);//tiempo de espera
  digitalWrite(ledVerde,LOW);
  delay(150);
  digitalWrite(motor,LOW);
  


}
