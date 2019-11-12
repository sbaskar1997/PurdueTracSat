#define LASERPIN 12

  const byte numChars = 32;
  char receivedChars[numChars];
  boolean newData = false;
  boolean inputRetreived = false;
  //String myText = "1,100,90,500#";
  String myText = receivedChars;
  int bits[500];
  int j;
  int size;
  void(* resetFunc) (void) = 0;
  
void setup() {
  // put your setup code here, to run once:
  pinMode(LASERPIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Waiting for data...");  
  while (inputRetreived == false){
    recvWithStartEndMarkers();
    showNewData();
  }
  String myText = receivedChars;
  
  j = 0;
  int position =  0;
  //Serial.println(myText.length());
  for(int i=0; i<myText.length(); i++){
    char myChar = myText.charAt(i);
    
    String binaryString = String((int) myChar, BIN);
    //Serial.println(binaryString);
    if (binaryString.length() < 8){
      for (int u = 0; u < 8 - binaryString.length(); u++){
        bits[position] = 0;
        position = position + 1;

      }
    }
    //Serial.println(bits[position]);
    for (int k = 0; k < binaryString.length(); k++){
      bits[position] = String(binaryString.charAt(k)).toInt();
      //Serial.println(bits[position]);
      position = position + 1;
      
    }
  }
   size = myText.length() * 8;
  int m = 0;
 for (int i=0; i < size; i++){
  Serial.print(bits[i]);
  if (!((i+1)%8) && i != 0){
    Serial.println(myText.charAt(m++));
  }
 }
 Serial.println("Starting...");
}


void loop() {
  // Start bit
  if (Serial.available() > 0 && Serial.read() == 48) {
    resetFunc();
  }
  digitalWrite(LASERPIN, HIGH);
  delay(1);
  digitalWrite(LASERPIN,LOW);
  for(int i = j; i < 8 + j; i++){
    digitalWrite(LASERPIN, bits[i]);
    //Serial.print(bits[i]);
    delayMicroseconds(1000);
  }
  j+=8;
  //Serial.print(" ");
  if (j >= size){
    //Serial.println("");
    j = 0;
  }
  digitalWrite(LASERPIN, LOW);
  delay(5);
}


void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
 // if (Serial.available() > 0) {
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("Inputted Message: ");
        Serial.println(receivedChars);
        inputRetreived = true;
        newData = false;
    }
}
