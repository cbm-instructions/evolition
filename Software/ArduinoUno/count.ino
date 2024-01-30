int in1 = 9;
int in2 = 8;
byte sensorPin_Slot = 2;
byte sensorPin_EndeR = 7;
byte sensorPin_EndeL = 5;

//für count
volatile int count = 0;
bool richtung = false; //false = links, true = rechts
int cheat = 0;
int countInt = 0;

//für Input
int input = 0;
int status = 0;
int wechsel = 0;
int lastInput = 0;


void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  pinMode(sensorPin_Slot, INPUT);
  pinMode(sensorPin_EndeL, INPUT);
  pinMode(sensorPin_EndeR, INPUT);
  Serial.begin(9600);
  
  startPosition();

  attachInterrupt(digitalPinToInterrupt(sensorPin_Slot), countInc, CHANGE);
  attachInterrupt(digitalPinToInterrupt(sensorPin_EndeL), saveLeft, CHANGE);
  attachInterrupt(digitalPinToInterrupt(sensorPin_EndeR), saveRight, CHANGE);
}

void startPosition(){
    while(!digitalRead(sensorPin_EndeL)) {
    linksDrehen();
  }
  stopp();
  count = 4;
  countInt = 4;
}

void loop() {
  if(Serial.available()) {
    String helpy = Serial.readStringUntil('\n');
    input = helpy.toInt();
  }

  if(input == 0) {
    input = lastInput;
  } else {
    lastInput = input;
  }

  switch (input){
    case 1: //Gandalf
      if(1 == countInt){
        saveRight();
        stopp();
      }else{
        richtung = false;
        while(countInt != 1){
          rechtsDrehen();
        }
      }
      break;
    case 2: //Klausur
      if(2 == countInt){
        stopp();
      }else if (2 > countInt){
        richtung = true;
        while(countInt != 2){
          linksDrehen();
        }
      } else {
        richtung = false;
        while(countInt != 2){
          rechtsDrehen();
        }
      }
      break;
    case 3: //Vorlesung
      if(3 == countInt){
        stopp();
      }else if (3 > countInt){
        richtung = true;
        while(countInt != 3){
          linksDrehen();
        }
      } else {
        richtung = false;
        while(countInt != 3){
          rechtsDrehen();
        }
      }
      break;
    case 4: //default
      if(4 == countInt){
        saveLeft();
        stopp();
      }else{
        richtung = true;
        while(countInt != 4){
          linksDrehen();
        }
      }
      break;
  }
}

void rechtsDrehen(){
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
}

void linksDrehen(){
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
}

void stopp() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}

#define precision 50

void countInc() {
  if(digitalRead(sensorPin_Slot) == HIGH) {
    unsigned long current = millis();
    static unsigned long last = 0;
    if((current - last) > precision) {
      if(richtung) {
        count++;
      } else {
        count--;
      }
      last = current;
    }
  countInt = count;
  }
}

void saveLeft() {
  if(digitalRead(sensorPin_EndeL) == HIGH) {
    stopp();
  }
}
void saveRight() {
  if(digitalRead(sensorPin_EndeR) == HIGH) {
    stopp();
  }
}