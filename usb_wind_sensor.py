import serial

# Open the serial port to the Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

while True:
    line = ser.readline().decode('utf-8').strip()  # read a line from Arduino
    if line:  # if line is not empty
        print("Received:", line)