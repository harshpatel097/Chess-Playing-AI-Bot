#include <Servo.h> 

//Variables

void arm_movement_empty();

void arm_movement_capture();

void angle_extraction(String move);

Servo shoulder;

Servo elbow;

Servo gripper;

Servo rack;

int i1=-1,i2=-1,j1=-1,j2=-1,empty;

int r=5;

int s=9;

int e=10;

int g=6;

int s_d=49;

int e_d=110;

int s_f=s_d;

int e_f=e_d;

int s_f2=s_d;

int e_f2=e_d;

int g_d=130;

int r_d=0;

int g_f=180;

int r_f=r_d;

int r_f2=r_d;

int r_f_d=110;

int shoulder_angle[][8]={{0,111,0,0,0,0,68,0},

                         {111,105,98,95,82,74,64,50.5},

                         {113,0,99.5,0,0,70,0,48},

                         {113,105,98,90,82,73,63,53},

                         {0,0,0,0,0,0,0,0},

                         {0,0,0,0,0,0,0,0},

                         {0,0,0,0,0,0,0,0},

                         {0,0,0,0,0,0,0,0}};

int elbow_angle[][8]={{0,110.5,0,0,0,0,138,0},

                      {98,103,113,120,125,130,134,139.5},

                      {96,0,112,0,0,126,0,134},

                      {93,100,104,107,119,121,125,128},

                      {0,0,0,0,0,0,0,0},

                      {0,0,0,0,0,0,0,0},

                      {0,0,0,0,0,0,0,0},

                      {0,0,0,0,0,0,0,0}};
int rack_angle[][8]={{150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150},
                     {150,150,150,150,150,150,150,150}};  
 
void setup() 

{ 

  Serial.begin(9600);

  //angle_extraction("h7h51");

  shoulder.attach(s);

  elbow.attach(e);

  gripper.attach(g);

  rack.attach(r);

  rack.write(r_d);

  gripper.write(g_d);

  shoulder.write(s_d);

  elbow.write(e_d);

  /*Serial.println(s_f);

  Serial.println(e_f);

  Serial.println(r_f);

  Serial.println(s_f2);

  Serial.println(e_f2);

  Serial.println(r_f2);*/

  // set servo to mid-point

} 



void loop() 

{

  if(Serial.available()>0)

  {

    String move=Serial.readString();
    if(move)
    {
    angle_extraction(move);

    if(empty==1)

    arm_movement_empty();

    else

    arm_movement_capture();
    }
  }

} 

void arm_movement_empty()

{

  

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

  delay(1000);

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

  delay(1000);

  for(int i=r_d;i<=r_f;i++)//rack coming down

  {rack.write(i);

  delay(25); 

  }

  delay(1000);

  for(int i=g_d;i<=g_f;i++)//gripper closing

  {gripper.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=r_f;i>=r_d;i--)//rack going up

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  if(s_f<s_f2)

  {

  for(int i=s_f;i<=s_f2;i++)//shoulder movement-pos1 to pos2

  {shoulder.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=s_f;i>=s_f2;i--)//shoulder movement-pos1 to pos2

  {shoulder.write(i);

  delay(25); 

  }

  }

  delay(1000);

  if(e_f<e_f2)

  {

  for(int i=e_f;i<=e_f2;i++)//elbow movement-pos1 to pos2

  {elbow.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=e_f;i>=e_f2;i--)//elbow movement-pos1 to pos2

  {elbow.write(i);

  delay(25); 

  }

  }

  

  delay(1000);

  for(int i=r_d;i<=r_f2;i++)//rack coming down

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=g_f;i>=g_d;i--)//gripper opening

  {gripper.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=r_f2;i>=r_d;i--)//rack going up

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  if(s_f2<s_d)

  {

  for(int i=s_f2;i<=s_d;i++)//shoulder movement-pos2 to default

  {shoulder.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=s_f2;i>=s_d;i--)//shoulder movement-pos2 to default

  {shoulder.write(i);

  delay(25); 

  }

  }

  delay(1000);

  if(e_f2<e_d)

  {

  for(int i=e_f2;i<=e_d;i++)//elbow movement-pos2 to default

  {elbow.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=e_f2;i>=e_d;i--)//elbow movement-pos2 to default

  {elbow.write(i);

  delay(25); 

  }

  }

  

  

}

void arm_movement_capture()

{

  if(s_d<s_f2)

  {

  for(int i=s_d;i<=s_f2;i++)//shoulder movement-default to pos2

  {shoulder.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=s_d;i>=s_f2;i--)//shoulder movement-default to pos2

  {shoulder.write(i);

  delay(25); 

  }

  }

  delay(1000);

  if(e_d<e_f2)

  {

  for(int i=e_d;i<=e_f2;i++)//elbow movement-default to pos2

  {elbow.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=e_d;i>=e_f2;i--)//elbow movement-default to pos2

  {elbow.write(i);

  delay(25); 

  }

  }

  delay(1000);

  for(int i=r_d;i<=r_f;i++)//rack coming down

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=g_d;i<=g_f;i++)//gripper closing

  {gripper.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=r_f;i>=r_d;i--)//rack going up

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  if(s_f2<s_d)

  {

  for(int i=s_f2;i<=s_d;i++)//shoulder movement-pos2 to default

  {shoulder.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=s_f2;i>=s_d;i--)//shoulder movement-pos2 to default

  {shoulder.write(i);

  delay(25); 

  }

  }

  delay(1000);

  if(e_f2<e_d)

  {

  for(int i=e_f2;i<=e_d;i++)//elbow movement-pos2 to default

  {elbow.write(i);

  delay(25); 

  }

  }

  else

  {

  for(int i=e_f2;i>=e_d;i--)//elbow movement-pos2 to default

  {elbow.write(i);

  delay(25); 

  }

  }

  for(int i=r_d;i<=r_f_d;i++)//rack coming down

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=g_f;i>=g_d;i--)//gripper opening

  {gripper.write(i);

  delay(15); 

  }

  delay(1000);

  for(int i=r_f_d;i>=r_d;i--)//rack going up

  {rack.write(i);

  delay(15); 

  }

  delay(1000);

  arm_movement_empty();

}

void angle_extraction(String move)

{

  

  char c1=move[0];

  char c2=move[2];

  char c3=move[1];

  char c4=move[3];

  empty=move[4]-'0';

  switch(c1)

  {

         case 'h':

         j1=0;

         break;

         case 'g':

         j1=1;

         break;

         case 'f':

         j1=2;

         break;

         case 'e':

         j1=3;

         break;

         case 'd':

         j1=4;

         break;

         case 'c':

         j1=5;

         break;

         case 'b':

         j1=6;

         break;

         case 'a':

         j1=7;

         break;

         default:

         j1=-1;

         break;

  }

  switch(c2)

  {

         case 'h':

         j2=0;

         break;

         case 'g':

         j2=1;

         break;

         case 'f':

         j2=2;

         break;

         case 'e':

         j2=3;

         break;

         case 'd':

         j2=4;

         break;

         case 'c':

         j2=5;

         break;

         case 'b':

         j2=6;

         break;

         case 'a':

         j2=7;

         break;

         default:

         j2=-1;

         break;

  }

  switch(c3)

  {

         case '8':

         i1=0;

         break;

         case '7':

         i1=1;

         break;

         case '6':

         i1=2;

         break;

         case '5':

         i1=3;

         break;

         case '4':

         i1=4;

         break;

         case '3':

         i1=5;

         break;

         case '2':

         i1=6;

         break;

         case '1':

         i1=7;

         break;

         default:

         i1=-1;

         break;

  }

  switch(c4)

  {

         case '8':

         i2=0;

         break;

         case '7':

         i2=1;

         break;

         case '6':

         i2=2;

         break;

         case '5':

         i2=3;

         break;

         case '4':

         i2=4;

         break;

         case '3':

         i2=5;

         break;

         case '2':

         i2=6;

         break;

         case '1':

         i2=7;

         break;

         default:

         i2=-1;

         break;

  }

  s_f=shoulder_angle[i1][j1];

  e_f=elbow_angle[i1][j1];

  r_f=rack_angle[i1][j1];

  s_f2=shoulder_angle[i2][j2];

  e_f2=elbow_angle[i2][j2];

  r_f2=rack_angle[i2][j2];

 

  return;

}
