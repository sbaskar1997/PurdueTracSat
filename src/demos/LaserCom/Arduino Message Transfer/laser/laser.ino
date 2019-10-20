#define LASERPIN 12

  // 01011010
  //int bits[] = {LOW, HIGH, LOW, HIGH, HIGH, LOW, HIGH, LOW};
  String myText = "Tracsat";
  int bits[500];
  int j;
  int size;

  
void setup() {
  // put your setup code here, to run once:
  pinMode(LASERPIN, OUTPUT);

  
  j = 0;
  for(int i=0; i<myText.length(); i++){
    char myChar = myText.charAt(i);
    String binaryString = String((int) myChar, BIN);
    for (int k = 0; k < 8; k++){
      bits[i + k] = String(binaryString.charAt(k)).toInt();
    }
  }
   size = myText.length() * 8;
 for (int i; i > size; i++){
  Serial.print(bits[i]);
  if (!(i%8)){
     Serial.println("");
  }
 }
 }

void loop() {
  

  // Start bit
  digitalWrite(LASERPIN, HIGH);
  delay(10);
  digitalWrite(LASERPIN,LOW);
  
  for(int i = j; i < 8 + j; i++){
    digitalWrite(LASERPIN, bits[i]);
    delay(10);
  }
  j+=8;
  if (j >= size-8){
    j = 0;
  }
  
  
  digitalWrite(LASERPIN, LOW);

  delay(10);

}
