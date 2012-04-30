#include "mbed.h"
#include "mlx90614.h"

DigitalOut led(LED1); //displays I2C wait
I2C i2c(p28,p27);   //sda,scl
Serial pc(USBTX,USBRX);  //serial usb config

MLX90614 IR_thermometer(&i2c);

float temp; //temperature in degrees C

int main() {
    while (1) {
        led=1; //see if Thermo is working
        if (IR_thermometer.getTemp(&temp)) {
            led=0; //thermo is working
            //print temperature on PC
            printf("Temperature is %5.1F degrees C\r\n",temp);
        }
        
        //wait function
    }
}