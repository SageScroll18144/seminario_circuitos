double r1;
double r2 = 2200;
double x;

String ans;

void setup() {Serial.begin(9600);}

void loop() { 
  x = analogRead(A0)*0.0048828125;
  
  r1 = (5*r2/x)-r2;

  if(analogRead(A0) <= 0){
    Serial.println("None"); 
  }else if(r1>=1000){
    ans = String(r1/1000.0) + "  K Ohms | " + x + "V";
    Serial.println(ans); 
  }else{
    ans = String(r1) + "  Ohms | " + x + "V";
    Serial.println(ans);
  }
  delay(1000);
  
}
