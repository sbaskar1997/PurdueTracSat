#define LASERPIN 12
void setup() {
  // put your setup code here, to run once:
  pinMode(LASERPIN, OUTPUT);
  // 01011010
  int bits[] = {LOW, HIGH, LOW, HIGH, HIGH, LOW, HIGH, LOW};

}

void loop() {
  
  // Start bit
  digitalWrite(LASERPIN, HIGH);
  delay(10);
  digitalWrite(LASERPIN,LOW);

  for(int i = 0; i < 8; i++){
    digitalWrite(LASERPIN, bits[i]);
    delay(10);
  }

  digitalWrite(LASERPIN, LOW);

  delay(10);

}
