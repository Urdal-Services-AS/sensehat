from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

# Definerer farger
red = (255, 0, 0)
green = (0, 255, 0)

while True:
    # reading sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # avrunding av tall
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Create a message
    # str() converts the calue of a string so it can be cocatenated???
    message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

    # Logisk test for å definere bakgrunnsfarge
    if t > 25.0 and t < 37.8:
        bg = green
    else:
        bg = red
        
    # Display as message
    sense.show_message(message, scroll_speed=0.1, back_colour=bg)
    
    





