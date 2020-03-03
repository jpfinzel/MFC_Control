int incomingByte = 0; 
int activepin = 1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    if (incomingByte == 'A'){
      activepin = 3;
    }

    if (incomingByte == 'B'){
      activepin = 5;
    }

    if (incomingByte == 'C'){
      activepin = 6;
    }

    if (incomingByte == 'D'){
      activepin = 9;
    }

    if (incomingByte == 'E'){
      activepin = 10;
    }

    if (incomingByte == 'F'){
      activepin = 11;
    }
    analogWrite(activepin,incomingByte);
  }
}
