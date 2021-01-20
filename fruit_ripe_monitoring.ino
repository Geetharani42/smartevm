
#include <LiquidCrystal.h>
//#include <SoftwareSerial.h>
#include "DHT.h"
//SoftwareSerial SIM800(8, 7);  //RX,TX

#define DHTPIN 10     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11 
//#define mq5_sensor A0

#define buzzer 8

/**********************Application Related Macros**********************************/
#define         GAS_LPG             0   
#define         GAS_CO              1   
#define         GAS_SMOKE           2   

const int calibrationLed = LED_BUILTIN;                      //when the calibration start , LED pin 13 will light up , off when finish calibrating
const int MQ_PIN=A0;                                //define which analog input channel you are going to use
int RL_VALUE=5;                                     //define the load resistance on the board, in kilo ohms
float RO_CLEAN_AIR_FACTOR=9.83;                     //RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                                    //which is derived from the chart in datasheet
 
/***********************Software Related Macros************************************/
int CALIBARAION_SAMPLE_TIMES=50;                    //define how many samples you are going to take in the calibration phase
int CALIBRATION_SAMPLE_INTERVAL=500;                //define the time interal(in milisecond) between each samples in the
                                                    //cablibration phase
int READ_SAMPLE_INTERVAL=50;                        //define how many samples you are going to take in normal operation
int READ_SAMPLE_TIMES=5;                            //define the time interal(in milisecond) between each samples in 
                                                    //normal operation
 
 
 
/*****************************Globals***********************************************/
float           LPGCurve[3]  =  {2.3,0.21,-0.47};   //two points are taken from the curve. 
                                                    //with these two points, a line is formed which is "approximately equivalent"
                                                    //to the original curve. 
                                                    //data format:{ x, y, slope}; point1: (lg200, 0.21), point2: (lg10000, -0.59) 
float           COCurve[3]  =  {2.3,0.72,-0.34};    //two points are taken from the curve. 
                                                    //with these two points, a line is formed which is "approximately equivalent" 
                                                    //to the original curve.
                                                    //data format:{ x, y, slope}; point1: (lg200, 0.72), point2: (lg10000,  0.15) 
float           SmokeCurve[3] ={2.3,0.53,-0.44};    //two points are taken from the curve. 
                                                    //with these two points, a line is formed which is "approximately equivalent" 
                                                    //to the original curve.
                                                    //data format:{ x, y, slope}; point1: (lg200, 0.53), point2: (lg10000,  -0.22)                                                     
float           Ro           =  10;                 //Ro is initialized to 10 kilo ohms



bool humidity_flag=0;
bool temperature_flag=0;
bool CO2_flag=0;


const int rs = 12, en = 11, d4 = 6, d5 = 5, d6 = 4, d7 = 3;


LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
DHT dht(DHTPIN, DHTTYPE);

void setup() 
{

Serial.begin(9600);
dht.begin();

lcd.begin(16, 2);

//pinMode(LED_BUILTIN, OUTPUT);
pinMode(calibrationLed,OUTPUT);
digitalWrite(calibrationLed,HIGH);
pinMode(buzzer, OUTPUT);

digitalWrite(buzzer, LOW);

lcd.clear();
delay(10);
lcd.print("RIPENED FRUIT ");
delay(10);
lcd.setCursor(0, 1);
delay(10);
lcd.print("MONITORING SYS ");
delay(1000);
//give the sensor some time to calibrate
lcd.clear();
delay(10);
lcd.print("calibrating ");
lcd.setCursor(0, 1);
delay(10);
lcd.print("Sensors");
// for(int i = 0; i < 5; i++){
//      lcd.print(".");
//      delay(500);
//      }
Ro = MQCalibration(MQ_PIN);                         //Calibrating the sensor. Please make sure the sensor is in clean air         
digitalWrite(calibrationLed,LOW);   
//Serial.print("Ro= ");
//Serial.print(Ro);
//Serial.println("kohm");

lcd.clear();
delay(10);
lcd.print("SENSORS ACTIVE");
delay(1000);
lcd.clear();
delay(10);
lcd.print("SETTING UP GPRS ");
delay(3000);
//GPRS_setup();
lcd.setCursor(0, 1);
delay(10);
lcd.print("     DONE     ");
delay(1000);
}



void loop() 
{


//long iPPM_LPG = 0;
//long iPPM_Smoke = 0;
//iPPM_LPG = MQGetGasPercentage(MQRead(MQ_PIN)/Ro,GAS_LPG);
//iPPM_Smoke = MQGetGasPercentage(MQRead(MQ_PIN)/Ro,GAS_SMOKE);

float iPPM_CO = 0;
iPPM_CO = MQGetGasPercentage(MQRead(MQ_PIN)/Ro,GAS_CO);
//float gas= MQRead(MQ_PIN);
if(iPPM_CO>200000)
{
iPPM_CO=200000;  
}


//lcd.clear();
//delay(10);
//lcd.print("LPG: ");
//lcd.print(iPPM_LPG);
//lcd.print(" ppm");   
//   
//lcd.setCursor( 0,3 );
//lcd.print("Smoke: ");
//lcd.print(iPPM_Smoke);
//lcd.print(" ppm");    


// Reading temperature or humidity takes about 250 milliseconds!
// Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
float H = dht.readHumidity();
// Read temperature as Celsius (the default)
float T = dht.readTemperature();

if(H>100)
{
H=100;  
}
if(T>100)
{
T=100;  
}
 
if (isnan(H) || isnan(T))// || isnan(f)) 
{
  lcd.clear();
  delay(10);
  lcd.print("Failed to read from DHT sensor!");
    return;
}
lcd.clear();
lcd.print("T:");
delay(100);
lcd.print(T);

lcd.setCursor(9, 0);
lcd.print("H:");
delay(100);
lcd.print(H);

lcd.setCursor( 0, 1 );
lcd.print("GAS: ");
lcd.print(iPPM_CO);
//lcd.print(gas);
lcd.print(" ppm");

if(iPPM_CO>10000)    // CO2 levels in excess of 1% (10,000 ppm) will slow the ripening process
{
  lcd.clear();
lcd.print("FRUIT RIPENED ");
delay(1000);
if(CO2_flag==0)
{
CO2_flag=1;
digitalWrite(buzzer, HIGH);
sendsms("FRUIT RIPENED");
digitalWrite(buzzer, LOW);
lcd.setCursor( 0, 1 );
lcd.print("UPLOADING DATA..");
    
    GPRS_send(T,H,iPPM_CO);
    
}
}
if(T>50)
{
  lcd.clear();
lcd.print("HIGH TEMPERATURE");
delay(1000);
if(temperature_flag==0)
{
temperature_flag=1;
digitalWrite(buzzer, HIGH);
sendsms("HIGH TEMPERATURE");
digitalWrite(buzzer, LOW); 
lcd.setCursor( 0, 1 );
lcd.print("UPLOADING DATA...");

    GPRS_send(T,H,iPPM_CO);
    
}
}
if(H>80)
{
  lcd.clear();
lcd.print("HIGH HUMIDITY");
delay(1000);
if(humidity_flag==0)
{
humidity_flag=1;
digitalWrite(buzzer, HIGH);
sendsms("HIGH HUMIDITY");
digitalWrite(buzzer, LOW); 
lcd.setCursor( 0, 1 );
lcd.print("UPLOADING DATA...");
 
    GPRS_send(T,H,iPPM_CO);
    
}
}
if((H<80) && (T<50) && (iPPM_CO<10000))
{
 humidity_flag=0;
 temperature_flag=0;
 CO2_flag=0;
}

delay(200); 
}


void sendsms(const char *message)
{
   lcd.setCursor(0, 1);
  delay(10);
  lcd.print("SENDING SMS      ");
  delay(500);
  
  Serial.println("AT\r\n");
  delay(2000);
  Serial.println("ATE0\r\n");
  delay(2000);
 Serial.println("AT+CMGF=1\r\n");
 delay(2000);
  Serial.println("AT+CMGS=\"09074598671\"");
  delay(1000);
   Serial.print(message);
  delay(1000);
  Serial.println((char)26);
 
  delay(1000);
}

void GPRS_send(float a,float b,float c)
{

Serial.println("AT");
delay(1000);
Serial.println("AT+CPIN?");//check for sim
delay(1000);
Serial.println("AT+CREG?"); // checking sim registeration
delay(1000); 
Serial.println("AT+CGATT?");//checking if MS is connected to GPRS
delay(1000);
Serial.println("AT+CIPSHUT");
delay(1000); 
Serial.println("AT+CIPSTATUS"); // current connection status
delay(2000);
Serial.println("AT+CIPMUX=0");// start multiconnection
delay(2000);
Serial.println("AT+CSTT=\"airtelgprs.com\"");// APN of the sim
delay(1000);
Serial.println("AT+CIICR ");// start wireless connection with GPRS
delay(3000);
Serial.println("AT+CIFSR ");//get local IP address
delay(1000); 
Serial.println("AT+CIPSPRT=0");
delay(3000); 
Serial.println("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");// start TCP connection AT+HTTPPARA=\"URL\",\"api.thingspeak.com/update\"
delay(5000);  
Serial.println("AT+CIPSEND");// send data through TCP/UDP connection
delay(5000);
String str="GET https://api.thingspeak.com/update?api_key=PESQLADSZ6S92RM0&field2=" +String(a)+"&field3=" +String(b)+"&field4=" +String(c); 
Serial.print(str);
Serial.println();
delay(3000);
Serial.write(26);
delay(1000); 
Serial.println();
Serial.println("AT+CIPSHUT");
delay(1000); 
}


/****************** MQResistanceCalculation ****************************************
Input:   raw_adc - raw value read from adc, which represents the voltage
Output:  the calculated sensor resistance
Remarks: The sensor and the load resistor forms a voltage divider. Given the voltage
         across the load resistor and its resistance, the resistance of the sensor
         could be derived.
************************************************************************************/ 
float MQResistanceCalculation(int raw_adc)
{
  return ( ((float)RL_VALUE*(1023-raw_adc)/raw_adc));
}
 
/***************************** MQCalibration ****************************************
Input:   mq_pin - analog channel
Output:  Ro of the sensor
Remarks: This function assumes that the sensor is in clean air. It use  
         MQResistanceCalculation to calculates the sensor resistance in clean air 
         and then divides it with RO_CLEAN_AIR_FACTOR. RO_CLEAN_AIR_FACTOR is about 
         10, which differs slightly between different sensors.
************************************************************************************/ 
float MQCalibration(int mq_pin)
{
  int i;
  float val=0;

  for (i=0;i<CALIBARAION_SAMPLE_TIMES;i++) {            //take multiple samples
    val += MQResistanceCalculation(analogRead(mq_pin));
   
    delay(CALIBRATION_SAMPLE_INTERVAL);
    if(i<10)
    {
       lcd.print(".");
    }
  }
  val = val/CALIBARAION_SAMPLE_TIMES;                   //calculate the average value
  val = val/RO_CLEAN_AIR_FACTOR;                        //divided by RO_CLEAN_AIR_FACTOR yields the Ro                                        
  return val;                                                      //according to the chart in the datasheet 

}
 
/*****************************  MQRead *********************************************
Input:   mq_pin - analog channel
Output:  Rs of the sensor
Remarks: This function use MQResistanceCalculation to caculate the sensor resistenc (Rs).
         The Rs changes as the sensor is in the different consentration of the target
         gas. The sample times and the time interval between samples could be configured
         by changing the definition of the macros.
************************************************************************************/ 
float MQRead(int mq_pin)
{
  int i;
  float rs=0;
 
  for (i=0;i<READ_SAMPLE_TIMES;i++) {
    rs += MQResistanceCalculation(analogRead(mq_pin));
    delay(READ_SAMPLE_INTERVAL);
  }
 
  rs = rs/READ_SAMPLE_TIMES;
 
  return rs;  
}
 
/*****************************  MQGetGasPercentage **********************************
Input:   rs_ro_ratio - Rs divided by Ro
         gas_id      - target gas type
Output:  ppm of the target gas
Remarks: This function passes different curves to the MQGetPercentage function which 
         calculates the ppm (parts per million) of the target gas.
************************************************************************************/ 
float MQGetGasPercentage(float rs_ro_ratio, int gas_id)
{
  if ( gas_id == GAS_LPG ) {
     return MQGetPercentage(rs_ro_ratio,LPGCurve);
  } else if ( gas_id == GAS_CO ) {
     return MQGetPercentage(rs_ro_ratio,COCurve);
  } else if ( gas_id == GAS_SMOKE ) {
     return MQGetPercentage(rs_ro_ratio,SmokeCurve);
  }    
 
  return 0;
}
 
/*****************************  MQGetPercentage **********************************
Input:   rs_ro_ratio - Rs divided by Ro
         pcurve      - pointer to the curve of the target gas
Output:  ppm of the target gas
Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm) 
         of the line could be derived if y(rs_ro_ratio) is provided. As it is a 
         logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic 
         value.
 Y - y1 = m( X - x1)

X= (y-y1)/m + x1

X= (Rs/Ro-y1)/m + x1

log X =(log (Rs/Ro) - y1)/m +x1

X =10^( (log (Rs/Ro) - y1)/m +x1)

*Note: X = ppm on the graph

Y= Rs/Ro
************************************************************************************/ 
float  MQGetPercentage(float rs_ro_ratio, float *pcurve)
{
  return (pow(10,( ((log(rs_ro_ratio)-pcurve[1])/pcurve[2]) + pcurve[0])));


}
