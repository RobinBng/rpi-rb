from gpiozero import Button
from gpiozero import LED

button = Button(27, bounce_time=0.1)
led = LED(17)

while True:
    if button.is_pressed:
        print("The button was pressed!")
        led.on()
    else:
        print("The button was released!")
        led.off()
