#include <Servo.h>



Servo myservo;                              // create servo object to control a servo

int angle;                                  // variable to read the value from the analog pin



void setup() {

  // myservo.attach(9);                        // attaches the servo on pin 9 to the servo object
  pinMode(13, OUTPUT);     

  Serial.begin(9600);

}



void loop()

{

  while (Serial.available() > 0)

  {

    String angle = Sial.readString();
    if (angle=="e7e51")
      {
      digitalWrite(13, HIGH);
      delay(1000);
      digitalWrite(13, LOW);
      delay(1000);
      }

    //  Serial.print("angle=");

    //  Serial.println(angle);

    //  myservo.write(angle);              // sets the servo position according to the scaled value

      delay(15);                         // waits for the servo to get there

    }

}


