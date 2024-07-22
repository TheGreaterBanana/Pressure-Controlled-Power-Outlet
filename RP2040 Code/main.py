

from machine import ADC
import utime



analog_value = ADC(26)




while 1==1:
    reading = analog_value.read_u16() * 5 / 65535 
    print("ADC: ",reading)
    utime.sleep(0.2)