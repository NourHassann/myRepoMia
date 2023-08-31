#define width = 0.5
#define length =0.5
#define EN 7
#define EN2 12
const int frontSensor = 2;
const int backSensor = 3;
const int rightSensor  = 4;
const int leftSensor = 5;
int motor1a = 6;
int motor1b = 9;
int motor2a = 10;
int motor2b = 11;

int x= 0;
int y = 0;
int front_distance;
int back_distance;
int right_distance;
int left_distance;

void setup()
{
Serial.begin(9600);
pinMode(frontSensor,INPUT);
pinMode(backSensor,INPUT);
pinMode(rightSensor4,INPUT);
pinMode(leftSensor,INPUT);
pinMode(motor1a, OUTPUT);
pinMode(motor1b, OUTPUT);
pinMode(motor2a, OUTPUT);
pinMode(motor2b, OUTPUT);
}
void loop()
{
  if(localizeRobot(frontSensor) >0){
    forwardMoving();
    if(localizeRobot(frontSensor) = 5.5) 
    Serial.print("we find the robot");
  }
  if (localizeRobot(frontSensor) =0){
    if(localizeRobot(leftSensor) >0){
    LeftMoving();
   if(localizeRobot(frontSensor) = 4.5) 
    Serial.print("we find the robot");
    }
    else if(localizeRobot(rightSensor) >0){
    RightMoving();  
    if(localizeRobot(frontSensor) = 4.5) 
    Serial.print("we find the robot");}
  }

  
      }
    void forwardMoving(){
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  digitalWrite(motor2a, HIGH);
  digitalWrite(motor2b, LOW);
    }
    void backWardMoving(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, HIGH);
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, HIGH);
    }
    void LeftMoving(){
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, HIGH);
    }
    void RightMoving(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, HIGH);
  digitalWrite(motor2a, HIGH);
  digitalWrite(motor2b, LOW);
    }
    }
    int localizeRobot(sensor_Pin){
    digitalWrite(sensor_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(sensor_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sensor_pin, LOW);
  long duration = pulseIn(sensor_pin, HIGH);
  int distance = duration * 0.034 / 2;
    return distance;
      }