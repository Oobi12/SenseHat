from sense_hat import SenseHat #imports the SenseHat
sense=SenseHat()


charx=0  #Creates initial values for the x and y axis
chary=0

sense.set_pixel(1,2,(255,100,0)) #Assigns color values to pixels
sense.set_pixel(1,4,(255,100,0))
sense.set_pixel(1,6,(255,100,0))
sense.set_pixel(2,4,(255,100,0))
sense.set_pixel(2,7,(255,100,0))
sense.set_pixel(3,6,(255,100,0))
sense.set_pixel(3,3,(255,100,0))
sense.set_pixel(4,5,(255,100,0))
sense.set_pixel(4,7,(255,100,0))
sense.set_pixel(5,2,(255,100,0))
sense.set_pixel(5,4,(255,100,0))
sense.set_pixel(6,2,(255,100,0))
sense.set_pixel(6,6,(255,100,0))
sense.set_pixel(6,1,(255,100,0))
sense.set_pixel(7,4,(255,100,0))
sense.set_pixel(7,5,(255,100,0))
sense.set_pixel(7,3,(255,100,0))


while True:
    for event in sense.stick.get_events():   #Creates joystick system to correspond to direction
        if event.action == 'pressed' and event.direction == 'right':
            charx += 1
            sense.set_pixel(charx,chary,(101,67,33))
            test=charx-1
            sense.set_pixel(test,chary,(0,0,0)) #Deletes the color in the previous box. Clears it
        if event.action == 'pressed' and event.direction == 'left':
            charx -= 1
            sense.set_pixel(charx,chary,(101,67,33))
            test=charx+1
            sense.set_pixel(test,chary,(0,0,0))
        if event.action == 'pressed' and event.direction == 'up':
            chary += 1
            sense.set_pixel(charx,chary,(101,67,33))
            beep=chary-1
            sense.set_pixel(charx,beep,(0,0,0))
        if event.action == 'pressed' and event.direction == 'down':
            chary -= 1
            sense.set_pixel(charx,chary,(101,67,33))
            beep=chary+1
            sense.set_pixel(charx,beep,(0,0,0))
            

    
            


                
            