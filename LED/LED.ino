int led = 18;
int button = 2;

void setup() {
  // put your setup code here, to run once:
pinMode(led,OUTPUT);
pinMode(button,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(led,HIGH);
delay(300);
digitalWrite(led,LOW);
delay(300)
}
