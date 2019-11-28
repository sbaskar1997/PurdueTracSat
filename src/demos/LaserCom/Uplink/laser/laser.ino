#define LASERPIN 12

  const byte numChars = 132;
  char receivedChars[numChars];
  boolean newData = false;
  boolean inputRetreived = false;
  int bits[500];
  int byteIndex;
  int size;
  void(* resetFunc) (void) = 0;
  
void setup() {
  // Setup code
  pinMode(LASERPIN, OUTPUT);
  Serial.begin(9600);

  //Wait for serial input.
  Serial.println("Waiting for data...");  
  while (inputRetreived == false){
    recvWithStartEndMarkers();
    showNewData();
  }
  String serialInput = receivedChars;
 
  convertToBinary(serialInput);
  Serial.println("Starting...");
}


void loop() {
  
  //If '0' is inputted in the serial monitor, then the program will reset for a different set of data to be inputted. 
  if (Serial.available() > 0 && Serial.read() == 48) {
    resetFunc();
  }

  //Start flash
  digitalWrite(LASERPIN, HIGH);
  delay(1);
  digitalWrite(LASERPIN,LOW);

  //Send one byte
  for(int i = byteIndex; i < 8 + byteIndex; i++){
    digitalWrite(LASERPIN, bits[i]);
    //Serial.print(bits[i]);
    delayMicroseconds(1000);
  }
  byteIndex+=8;
  //Serial.print(" ");

  //Reset the byteIndex back to 0 when the serialInput has been fully sent
  if (byteIndex >= size){
    //Serial.println("");
    byteIndex = 0;
  }

  //Delay between bytes.
  digitalWrite(LASERPIN, LOW);
  delay(5);
}

//Function to receive serial input
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

//Show serial input
void showNewData() {
    if (newData == true) {
        Serial.print("Inputted Message: ");
        Serial.println(receivedChars);
        inputRetreived = true;
        newData = false;
    }
}

//Convert serial input to binary
void convertToBinary(String serialInput){
  byteIndex = 0;
  int position =  0;
  size = serialInput.length() * 8;
  int printIndex = 0;
  
  //Serial.println(serialInput.length());
  for(int i=0; i<serialInput.length(); i++){
    char myChar = serialInput.charAt(i);
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

  //Print all bytes for visual inspection
  for (int i=0; i < size; i++){
    Serial.print(bits[i]);
    if (!((i+1)%8) && i != 0){
      Serial.println(serialInput.charAt(printIndex++));
    }
  }
}
