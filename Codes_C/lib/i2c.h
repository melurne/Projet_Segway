#ifndef __I2C_H__
#define __I2C_H__

#define ADDR_MCU 0x20

typedef struct i2c_message_s {

} i2c_message_t;

int connectI2C();
i2c_message_t recvi2c();


#endif