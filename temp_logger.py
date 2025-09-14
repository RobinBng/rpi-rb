from gpiozero import Button
import sys, time, threading

# Get output filename from command line
if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <output_filename>")
    sys.exit("Failed to launch. need command line argument")
output = sys.argv[1]


# Setup button
button = Button(27, bounce_time=0.1)
stop_flag = False

def button_thread():
    global stop_flag
    while not stop_flag:
        if button.is_pressed:
            print("Button pressed! Stopping program...")
            stop_flag = True
        time.sleep(0.05)  # check every 50ms


# Read temperature from 1w sensor
input_temp = "/sys/bus/w1/devices/28-0319163131e5/temperature"
def read_temp():
    try:
        with open(input_temp, 'r') as file:
            return float(file.read()) / 1000
    except (ValueError, FileNotFoundError, OSError):
        print("Temperature sensor disconnected or invalid value")
        return None


# Start button thread
threading.Thread(target=button_thread, daemon=True).start()

# Open output file and log temperature
with open(output, 'w') as log:
    print(f"Logging temperature to {output}. Press button to stop.")
    while not stop_flag:
        temp = read_temp()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log.write(f"{timestamp}, Temp: {temp:.2f}°C\n")
        #print(f"{timestamp} -> {temp:.2f} °C")
        time.sleep(1)

print("File closed.")





