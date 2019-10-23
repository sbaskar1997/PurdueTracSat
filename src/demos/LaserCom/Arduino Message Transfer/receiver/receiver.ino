#define SOLARPIN A0
#define THRESHOLD 10

int ascii = 0;
int ambientReading = 10;
int k = 1;

void setup() {
  // put your setup code here, to run once:
  pinMode(SOLARPIN, INPUT);
  Serial.begin(9600);
  ambientReading = analogRead(SOLARPIN);
}

void loop() {
  
  int reading = analogRead(SOLARPIN);
  int bits[8];

  
  if (reading > ambientReading + THRESHOLD) {
    delay(10);
    for (int i = 0; i < 8; i++){
      if (analogRead(SOLARPIN) > ambientReading + THRESHOLD){
        bits[i] = 1;
      } else{
        bits[i] = 0;
      }
      delay(1);
    }
  
    
    /*
    for (int l = 0; l < 8; l++){
      Serial.print(bits[l]);
    }
    Serial.println("");
    */
    
    int i = 0;
    int len  = 8;
    double sum = 0;
    int j = 0;
    
    for(i=(len-1);i>=0;i--)
    {
        sum = sum +  (pow(2,i) * (bits[j]));
        j++;
    }
    char aChar = (int) lround(sum);
    Serial.print(aChar);

    
    if (k++ == 7){
      Serial.println("");
    }
  }

}
