import time

import serial

ser = serial.Serial("COM4", 115200, timeout=1)
time.sleep(1)

# Force ESP32 reset (DTR/RTS toggle)
ser.dtr = False
ser.rts = False
time.sleep(0.2)

ser.dtr = True
ser.rts = True
time.sleep(0.2)

ser.dtr = False
ser.rts = False

ser.close()
print("Reset sent")
