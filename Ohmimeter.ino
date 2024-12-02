double r1;
double r2 = 2200;
double x;
void setup() {Serial.begin(9600);}

void loop() { 
  x = analogRead(A0)*0.0048828125;
  
  r1 = (5*r2/x)-r2;
  if (analogRead(A0) > 0) Serial.println(r1);
  else Serial.println("-1");
  delay(1000);
}
