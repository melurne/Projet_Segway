#include "global.h"

void *getter(void * args) {
    int fd;
    fd = wiringPiI2CSetup(ADDR_MCU);
    while (1) {
        int wiringPiI2CRead(fd);
    }

}