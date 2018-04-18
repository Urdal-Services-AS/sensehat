from sense_hat import SenseHat
import math

sense = SenseHat()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x=round(x, 8)
    y=round(y, 8)
    z=round(z, 8)
    
    try:
        V1=abs(z/x)
    except ZeroDivisionError: pass
    
    #try:
    #    V2=abs(z/y)
    #except ZeroDivisionError: pass
   
    # Altertnativ print hvis ikke vinkel
    # print("x=" + str(x),"y=" + str(y),"z=" + str(z))
    
    Vinkel1 = int(90 + math.degrees(math.atan(V1)) * -1)
    #Vinkel2 = round(90 + math.degrees(math.atan(V2)) * -1, 3)
    
    print(" Vinkel 1 = " + str(Vinkel1))
          #+ " Vinkel 2 = " + str(Vinkel2))

    # Display accelerometer:
    # define rgb
    r=int(2.8*Vinkel1)
    g=int(0)
    b=255-(int(2.8*Vinkel1))
    
    
    sense.show_message(str(Vinkel1), back_colour=(r, g, b))
    