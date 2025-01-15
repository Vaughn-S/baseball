#Vaughn Smith
#Estimated Pitch Separation Version 1

#Program
import math as m

def main():
    #Input Variables
    ext = float(input('Enter player extension for pitch 1: '))                           #Extension in feet for pitch 1
    ext2 = float(input('Enter player extension for pitch 2: '))                          #Extension in feet for pitch 2
    v1 = float(input('Enter the velocity of pitch 1: '))
    v2 = float(input('Enter the velocity of pitch 2: '))

    xmov1 = float(input('Enter the horizontal movement of pitch 1: '))                   #Horizontal movement (displacement) in inches at plate
    ymov1 = float(input('Enter the vertical drop of pitch 1: '))                         #Vertical movement (displacement) in inches w/ gravity at plate
    xmov2 = float(input('Enter the horizontal movement of pitch 2: '))
    ymov2 = float(input('Enter the vertical drop of pitch 2: ')) 

    #Constants
    DIST = 60.5                   #Distance from mound to home in feet
    FT_TO_MI = 5280               #Conversion factor b/t feet and miles
    S_TO_HR = 3600                #Conversion factor b/t hours and seconds

    #Pitch 1 Estimated Time to plate
    dist = DIST - ext                                         #Distance traveled by pitch 1 in feet
    dist_2 = DIST - ext2                        
    t1 = S_TO_HR/(v1*FT_TO_MI)*dist                           #Time to plate for pitch 1; represents time of measurment
    t2 = S_TO_HR/(v2*FT_TO_MI)*dist                           #Time to plate for pitch 2

    dist2 = v2*FT_TO_MI/S_TO_HR*t1+(dist_2-dist)              #Distance traveled by pitch 2 at t1

    #Displacement of Pitch 1 at t = t1
    xdisp1 = xmov1                              #Horizontal displacement of pitch 1
    ydisp1 = ymov1                              #Vertical displacement of pitch 1

    #Displacement of Pitch 2 at t = t1
    #Because of constant acceleration, null initial velocity, and null initial displacement
    #a = (2*x)/t^2 where x is change in position (delta x)
    #x = 1/2at^2 where x is the change in position

    x_accel2 = (2*xmov2)/t2**2                   #Horizontal acceleration of pitch 2
    xdisp2 = 0.5*x_accel2*t1**2                  #Horizontal displacement of pitch 2 at t1
    y_accel2 = (2*ymov2)/t2**2                   #Vertical acceleration of pitch 2
    ydisp2 = 0.5*y_accel2*t1**2                  #Vertical displacement of pitch 2 at t1

    #distance between pitches
    x_sep = xdisp2 - xdisp1                     #+/- mean glove/arm side displacement respectively for pitch 2 relative pitch 1
    y_sep = ydisp2 - ydisp1                     #+/- mean upward/downward displacement respecitively for pitch 2 relative ptich 1
    z_sep = dist - dist2                        #always negative

    xyz_sep = m.sqrt(x_sep**2 + y_sep**2 + z_sep**2)

    print (f'\nPitch 1 had a horizontal displacement of {xdisp1:.2f} inches')
    print (f'Pitch 1 had a vertical displacement of {ydisp1:.2f} inches')
    print (f'\nPitch 2 had a horizontal dispalcement of {xdisp2:.2f} inches')
    print (f'Pitch 2 had a vertical displacement of {ydisp2:.2f} inches')
    print (f'\nThe horizontal seperation between the two pitches was {x_sep:.2f} inches')
    print (f'The vertical separation between the two pitches was {y_sep:.2f} inches')
    print (f'The z-axis separation between the two pitches was {z_sep:.2f} inches')
    print (f'\nThe total liner separation between the two pitches was {xyz_sep:.2f} inches')

main()