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
  Serial.begin(9600);
  
  j = 0;
  int position =  0;
  for(int i=0; i<myText.length(); i++){
    char myChar = myText.charAt(i);
    
    String binaryString = String((int) myChar, BIN);
    //Serial.println(binaryString);
    bits[position] = 0;
    position = position + 1;
    //Serial.println(bits[position]);
    for (int k = 0; k < 7; k++){
      bits[position] = String(binaryString.charAt(k)).toInt();
      //Serial.println(bits[position]);
      position = position + 1;
      
    }
  }
   size = myText.length() * 8;


   
 for (int i=0; i < size; i++){
  Serial.print(bits[i]);
 }
 Serial.println("real");
}


void loop() {
  

  // Start bit
  digitalWrite(LASERPIN, HIGH);
  delay(10);
  digitalWrite(LASERPIN,LOW);
  
  for(int i = j; i < 8 + j; i++){
    digitalWrite(LASERPIN, bits[i]);
    //Serial.print(bits[i]);
    
    delay(1);
  }
  j+=8;
  //Serial.print(" ");
  if (j >= size){
    //Serial.println("");
    j = 0;
  }
  
  
  digitalWrite(LASERPIN, LOW);

  delay(10);

}
