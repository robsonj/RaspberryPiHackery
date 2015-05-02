#!/usr/bin/python

import wiringpi
from time import sleep

port = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(port, 1)
wiringpi.digitalWrite(port, 1)
wiringpi.digitalWrite(port, 0)
sleep(1)
wiringpi.digitalWrite(port, 1)
