from __future__ import division
import time
import Adafruit_PCA9685
from forecastiopy import *

Locations= {"RighterHand":0,"RightHand":1,"RightArm":2,
"LefterHand":3,"LeftHand":4,"LeftArm":5,
"LeftLeg":7,"RightLeg":6,
"LeftFootBoxUper":10,"LeftFootBoxUp":11,
"RightFootBoxUper":8,"RightFootBoxUp":9,
"LeftMiddle":None,"RightMiddle":None,
"LeftFootBoxDowner":15,"LeftFootBoxDown":14,
"RightFootBoxDowner":13,"RightFootBoxDown":12,
}
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
pwm.set_pwm_freq(60)
def ServoAngleSet(Serv,Angle):
    pwm.set_pwm(Serv, 0, Angle2Pulse(Angle))
def Move_RightHand():
    pwm.set_pwm(Locations['RighterHand'], 0, 375)
    time.sleep(0.3)
    pwm.set_pwm(Locations['RightHand'], 0, 375)
    time.sleep(0.3)
    pwm.set_pwm(Locations['RightArm'], 0, servo_max)
    time.sleep(0.3)
    pwm.set_pwm(Locations['RightArm'], 0, servo_min)
    time.sleep(0.3)
    pwm.set_pwm(Locations['RightArm'], 0, servo_max)
    time.sleep(0.3)
    pwm.set_pwm(Locations['RightArm'], 0, servo_min)
    time.sleep(0.3)
    Free()
def Move_LeftHand():
    pwm.set_pwm(Locations['LefterHand'], 0, 375)
    time.sleep(0.3)
    pwm.set_pwm(Locations['LeftHand'], 0, 375)
    time.sleep(0.3)
    pwm.set_pwm(Locations['LeftArm'], 0, servo_max)
    time.sleep(0.3)
    pwm.set_pwm(Locations['LeftArm'], 0, servo_min)
    time.sleep(0.3)
    pwm.set_pwm(Locations['LeftArm'], 0, servo_max)
    time.sleep(0.3)
    pwm.set_pwm(Locations['LeftArm'], 0, servo_min)
    time.sleep(0.3)
    Free()
def Free():
    pwm = Adafruit_PCA9685.PCA9685()
def CheckAngles():
    Serv=int(input("Servo : "))
    try:
        while True:
            pwm.set_pwm(Serv, 0, Angle2Pulse(int(input("Angle = "))))
    except:
        Free()
def Angle2Pulse(Angle):
    return int(((600-150)/180*Angle)+150)
def Clap(Times):
    ServoAngleSet(Locations["RightArm"],150)
    ServoAngleSet(Locations["LeftArm"],180)
    ServoAngleSet(Locations["RightHand"],0)     #-10
    ServoAngleSet(Locations["LeftHand"],160)    #180
    ServoAngleSet(Locations["RighterHand"],0)
    ServoAngleSet(Locations["LefterHand"],0)    #UnKnown
    time.sleep(1)
    Free()
    for i in range(Times):
        ServoAngleSet(Locations["RightHand"],-10)     #-10  --  0
        ServoAngleSet(Locations["LeftHand"],180)    #180  --  160
        time.sleep(0.6)
        ServoAngleSet(Locations["RightHand"],0)     #-10  --  0
        ServoAngleSet(Locations["LeftHand"],160)    #180  --  160
        time.sleep(0.6)

        
    #  -------S  T   A   B   L   E-------
    ServoAngleSet(Locations["RighterHand"],90)
    ServoAngleSet(Locations["LefterHand"],90)
    time.sleep(0.5)
    
    ServoAngleSet(Locations["RightArm"],90)
    ServoAngleSet(Locations["LeftArm"],105)

    ServoAngleSet(Locations["RightHand"],0)   
    ServoAngleSet(Locations["LeftHand"],160)    

    time.sleep(1)
    Free()
def Fly(Times):
    ServoAngleSet(Locations["LefterHand"],90)
    ServoAngleSet(Locations["RighterHand"],90)
    ServoAngleSet(Locations["RightArm"],90)
    ServoAngleSet(Locations["LeftArm"],105)
    time.sleep(1)
    Free()

    for i in range (Times):
    
        for a in range (30,111):
            ServoAngleSet(Locations["RightHand"],155-a)
            ServoAngleSet(Locations["LeftHand"],a)
            time.sleep(0.001)
        for a in range (30,111):
            ServoAngleSet(Locations["RightHand"],140-(125-a))
            ServoAngleSet(Locations["LeftHand"],140-a)
            time.sleep(0.001)
    time.sleep(0.1)
    
    ServoAngleSet(Locations["RighterHand"],90)
    ServoAngleSet(Locations["LefterHand"],90)
    time.sleep(0.5)
    
    ServoAngleSet(Locations["RightArm"],90)
    ServoAngleSet(Locations["LeftArm"],105)

    ServoAngleSet(Locations["RightHand"],0)   
    ServoAngleSet(Locations["LeftHand"],160)    

    time.sleep(1)
    Free()
def DownStable(Sec):
    #Legs---Right THen Left
    ServoAngleSet(Locations["RightLeg"],95)
    ServoAngleSet(Locations["LeftLeg"],95)
    time.sleep(0.4)
    Free()
    
    #-----Right         ---Up To dOWN
    
    ServoAngleSet(Locations["RightFootBoxUper"],90)
    ServoAngleSet(Locations["RightFootBoxUp"],120)
    ServoAngleSet(Locations["RightFootBoxDown"],100)
    ServoAngleSet(Locations["RightFootBoxDowner"],135)

    #-----Left         ---Up To dOWN
    
    ServoAngleSet(Locations["LeftFootBoxUper"],90)
    ServoAngleSet(Locations["LeftFootBoxUp"],110)
    ServoAngleSet(Locations["LeftFootBoxDown"],70)
    ServoAngleSet(Locations["LeftFootBoxDowner"],70)

    #-----Done
    
    time.sleep(Sec)

    Free()
def DownStableRight():
    #Legs---Right
    ServoAngleSet(Locations["RightLeg"],95)

    #-----Right         ---Up To dOWN
    
    ServoAngleSet(Locations["RightFootBoxUper"],90)
    ServoAngleSet(Locations["RightFootBoxUp"],120)
    ServoAngleSet(Locations["RightFootBoxDown"],100)
    ServoAngleSet(Locations["RightFootBoxDowner"],135)

    #-----Done
def DownStableLeft():
    #Legs---Left
    ServoAngleSet(Locations["LeftLeg"],95)
    
    #-----Left         ---Up To dOWN
    
    ServoAngleSet(Locations["LeftFootBoxUper"],90)
    ServoAngleSet(Locations["LeftFootBoxUp"],110)
    ServoAngleSet(Locations["LeftFootBoxDown"],70)
    ServoAngleSet(Locations["LeftFootBoxDowner"],70)

    #-----Done
