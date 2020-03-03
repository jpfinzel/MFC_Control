// Program variables ----------------------------------------------------------
int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
int sensorValue5 = 0;
int sensorValue6 = 0;

float value_1 = 0;
float value_2 = 0;
float value_3 = 0;
float value_4 = 0;
float value_5 = 0;
float value_6 = 0;

float flow1 = 50;
float flow2 = 50;
float flow3 = 50;
float flow4 = 50;
float flow5 = 50;
float flow6 = 50;

// Comma delimiter to separate consecutive data if using more than 1 sensor
const char kDelimiter = ',';  

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  processSensors();
  sendDataToSerial();
}

// SENSOR INPUT CODE-----------------------------------------------------------
void processSensors() 
{
  // read the input on analog pin 0:
  sensorValue1 = analogRead(A0);
  value_1 = sensorValue1 * (flow1 / 1023.0);

  sensorValue2 = analogRead(A1);
  value_2 = sensorValue2 * (flow2 / 1023.0);

  sensorValue3 = analogRead(A2);
  value_3 = sensorValue3 * (flow3 / 1023.0);

  sensorValue4 = analogRead(A3);
  value_4 = sensorValue4 * (flow4 / 1023.0);

  sensorValue5 = analogRead(A4);
  value_5 = sensorValue5 * (flow5 / 1023.0);

  sensorValue6 = analogRead(A5);
  value_6 = sensorValue6 * (flow6 / 1023.0);
  
  // Add any additional raw data analysis below (e.g. unit conversions)
  
}

// OUTGOING SERIAL DATA PROCESSING CODE----------------------------------------
void sendDataToSerial()
{
  // Send data out separated by a comma (kDelimiter)
  // Repeat next 2 lines of code for each variable sent:

  Serial.print(value_1);
  Serial.print(kDelimiter);
  Serial.print(value_2);
  Serial.print(kDelimiter);
  Serial.print(value_3);
  Serial.print(kDelimiter);
  Serial.print(value_4);
  Serial.print(kDelimiter);
  Serial.print(value_5);
  Serial.print(kDelimiter);
  Serial.print(value_6);
  Serial.print(kDelimiter);
  
  Serial.println(); // Add final line ending character only once
  //delay(1000);

  delay(500);
}
