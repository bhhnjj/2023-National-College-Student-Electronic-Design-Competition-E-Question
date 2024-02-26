# Find Rects Example
#
# This example shows off how to find rectangles in the image using the quad threshold
# detection code from our April Tags code. The quad threshold detection algorithm
# detects rectangles in an extremely robust way and is much better than Hough
# Transform based methods. For example, it can still detect rectangles even when lens
# distortion causes those rectangles to look bent. Rounded rectangles are no problem!
# (But, given this the code will also detect small radius circles too)...

from machine import Timer,PWM
from machine import Timer,PWM
from maix import GPIO
from fpioa_manager import fm
from board import board_info

import sensor, image, time
import lcd
import math

lcd.init()
lcd.clear(lcd.RED)
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster (160x120 max on CanMV-M7)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

tim1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
S1 = PWM(tim1, freq=50, duty=0, pin=19)

tim2 = Timer(Timer.TIMER0, Timer.CHANNEL1, mode=Timer.MODE_PWM)
S2 = PWM(tim2, freq=50, duty=0, pin=18)

def Servo1(servo,angle):
    S1.duty((angle+90)/180*10+2.5)


def Servo2(servo,angle):
    S2.duty((angle+90)/180*10+2.5)



while(True):
    clock.tick()
    img = sensor.snapshot()

    # `threshold` below should be set to a high enough value to filter out noise
    # rectangles detected in the image which have low edge magnitudes. Rectangles
    # have larger edge magnitudes the larger and more contrasty they are...

    for r in img.find_rects(threshold = 10000):
        img.draw_rectangle(r.rect(), color = (255, 0, 0))
        for p in r.corners(): img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
        #print(r)
        d = r.corners()
        q1=d[3]
        q2=d[2]
        q3=d[1]
        q4=d[0]

        x1=q1[0]
        y1=q1[1]

        x2=q2[0]
        y2=q2[1]

        x3=q3[0]
        y3=q3[1]
        x4=q4[0]
        y4=q4[1]

        x112=(x1+x2)/2
        y112=(y1+y2)/2



        x223=(x2+x3)/2
        y223=(y2+y3)/2


        x334=(x3+x4)/2
        y334=(y3+y4)/2


        x441=(x4+x1)/2
        y441=(y4+y1)/2



        #k1=(y2-y1)/(x2-x1)
        H=238
        L=80
        W=250

        xia = -7
        down = 1
        up=1
        shang= -9.2

        a1= xia + down * math.degrees(math.atan((L-x1)/H))
        a2= xia + down * math.degrees(math.atan((L-x2)/H))
        a3= xia + down * math.degrees(math.atan((L-x3)/H))
        a4= xia + down * math.degrees(math.atan((L-x4)/H))


        a112=xia + down * math.degrees(math.atan((L-x112)/H))

        a223=xia + down * math.degrees(math.atan((L-x223)/H))

        a334=xia + down * math.degrees(math.atan((L-x334)/H))

        a441=xia + down * math.degrees(math.atan((L-x441)/H))

        b1=shang- up * math.degrees(math.atan((120-y1)/W))
        b2=shang- up * math.degrees(math.atan((120-y2)/W))
        b3=shang- up * math.degrees(math.atan((120-y3)/W))
        b4=shang- up * math.degrees(math.atan((120-y4)/W))



        b112=shang- up * math.degrees(math.atan((120-y112)/W))

        b223=shang- up * math.degrees(math.atan((120-y223)/W))

        b334=shang- up * math.degrees(math.atan((120-y334)/W))

        b441=shang- up * math.degrees(math.atan((120-y441)/W))



        Servo1(S1,a1)
        Servo2(S2,b1)
        time.sleep(1)

        Servo1(S1,a112)
        Servo2(S2,b112)
        time.sleep(1)

        Servo1(S1,a2)
        Servo2(S2,b2)
        time.sleep(1)

        Servo1(S1,a223)
        Servo2(S2,b223)
        time.sleep(1)

        Servo1(S1,a3)
        Servo2(S2,b3)
        time.sleep(1)

        Servo1(S1,a334)
        Servo2(S2,b334)
        time.sleep(1)

        Servo1(S1,a4)
        Servo2(S2,b4)
        time.sleep(1)

        Servo1(S1,a441)
        Servo2(S2,b441)
        time.sleep(1)

    lcd.display(img)
