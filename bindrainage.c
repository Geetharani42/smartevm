#include<reg51.h>

void send (char *z);
void serial(unsigned char s);
void delay(unsigned int x);

sbit bin1=P2^2;
sbit bin2=P2^3;
sbit drainage=P2^4;
int c=1,d=1,e=1;

void main()
{
 TMOD=0x20;
TH1=0xFD;
SCON=0x50; 
TR1=1;
P2=0x00;
send ("AT \n");
delay(200);
send ("AT+CMGF=1 \n");
delay(200);
while(1)
{
 if(bin1==1&&c==1)
 {
  send ("AT+CMGS=\"8328034196\"\n\r");
delay(200);
send ("BIN1 is full\n");
delay(200);
serial (0x1a);
delay(200);
c=2;
 }
 else if(bin1==0&&c==2)
 {
  c=1;
  }
 
 if(bin2==1&&d==1)
 {
  send ("AT+CMGS=\"8328034196\"\n\r");
delay(200);
send ("BIN2 is full\n");
delay(200);
serial (0x1a);
delay(200);
d=2;
 }
 else if(bin2==0&&d==2)
 {
  d=1;
  }

 if(drainage==0&&e==1)
 {
  send ("AT+CMGS=\"8328034196\"\n\r");
delay(200);
send ("Manhole is open\n");
delay(200);
serial (0x1a);
delay(200);
e=2; 
 }
 else if(drainage==0&&e==2)
 {
  e=1;
  }
}
}
void delay(unsigned int x)
{
unsigned int i,j;
for(i=0;i<x;i++)
{
for(j=0;j<1275;j++);
}
}

void serial(unsigned char s)
{
SBUF=s;
while (TI==0);
TI=0;
}

void send(char *z)
{
unsigned int k;
for(k=0;z[k]!=0;k++)
{
serial (z[k]);
}
}
