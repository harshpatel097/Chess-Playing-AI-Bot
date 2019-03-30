#include <Servo.h> 



Servo shoulder;

Servo elbow;

void setup() 

{ 

  shoulder.attach(9);

  elbow.attach(10);

  int s_d=49;

  int e_d=110;

  int s_f=95;

  int e_f=120;

  int s_f2=115;

  int e_f2=102;

  shoulder.write(s_d);

  elbow.write(e_d);

  //delay(1000);

  if(s_d<s_f)

  {

  for(int i=s_d;i<=s_f;i++)//shoulder movement-default to pos1

  {shoulder.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=s_d;i>=s_f;i--)//shoulder movement-default to pos1

  {shoulder.write(i);

  delay(25); 

  }

  }

  delay(2000);

  if(e_d<e_f)

  {

  for(int i=e_d;i<=e_f;i++)//elbow movement-default to pos1

  {elbow.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=e_d;i>=e_f;i--)//elbow movement-default to pos1

  {elbow.write(i);

  delay(25); 

  }

  }


  delay(5000);

  if(s_f<s_f2)

  {

  for(int i=s_f;i<=s_f2;i++)//shoulder movement-pos1 to pos2

  {shoulder.write(i);

  delay(15); 

  }

  }

  else

  {

  for(int i=s_f;i>=s_f2;i--)//shoulder movement-pos1 to pos2

  {shoulder.write(i);

  delay(15); 

  }

  }

  delay(1000);

  if(e_f<e_f2)

  {

  for(int i=e_f;i<=e_f2;i++)//elbow movement-pos1 to pos2

  {elbow.write(i);

  delay(15); 

  }

  }

  else

  {

  for(int i=e_f;i>=e_f2;i--)//elbow movement-pos1 to pos2

  {elbow.write(i);

  delay(15); 

  }

  }



  delay(10000);

  if(s_f<s_d)

  {

  for(int i=s_f;i<=s_d;i++)//shoulder movement-pos1 to default

  {shoulder.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=s_f;i>=s_d;i--)//shoulder movement-pos1 to default

  {shoulder.write(i);

  delay(25); 

  }

  }

  delay(1000);

  if(e_f<e_d)

  {

  for(int i=e_f;i<=e_d;i++)//elbow movement-pos1 to default

  {elbow.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=e_f;i>=e_d;i--)//elbow movement-pos1 to default

  {elbow.write(i);

  delay(25); 

  }

  }

  

  

  // set servo to mid-point

} 



void loop() 

{

  

} 
