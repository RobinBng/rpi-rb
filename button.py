from gpiozero import Button

button = Button(27, bounce_time=0.1, )

while True:
	if button.is_pressed:
		
	print("The button was pressed!")
