#define SOLARPIN A0
#define THRESHOLD 30

int ascii = 0;
int ambientReading;
int k = 1;

void setup() {
  
  // Setup Code.
  pinMode(SOLARPIN, INPUT);
  Serial.begin(9600);
  ambientReading = analogRead(SOLARPIN);
  Serial.println(ambientReading);//Set the ambient reading of the receiver.
  
}

void loop() {
  
  int reading = analogRead(SOLARPIN);
  int bits[8];

  //When a start flash is read, an 8 bit loop begins. 
  if (reading > ambientReading + THRESHOLD) {
    delay(1);
    for (int i = 0; i < 8; i++){
      if (analogRead(SOLARPIN) > ambientReading + THRESHOLD){
        
        bits[i] = 1;
      } else{
        bits[i] = 0;
      }
     // Serial.println(analogRead(SOLARPIN));
    delayMicroseconds(1000);
    }
    convertToText(bits);
  }
}

//Convert array of bits to text. Outputted to serial monitor.
void convertToText(int bits[]){
    int i = 0;
    int j = 0;
    int len  = 8;
    double sum = 0;
    
    for(i=(len-1);i>=0;i--)
    {
        sum = sum +  (pow(2,i) * (bits[j]));
        j++;
    }
    char aChar = (int) lround(sum);
    Serial.print(aChar);

    if (aChar == '#'){
      Serial.println("");
    }
    /*
    for (int l = 0; l < 8; l++){
      Serial.print(bits[l]);
    }
    Serial.println("");*/
 }
