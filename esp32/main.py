from machine import Pin,Timer
#from machine import UART
import time
#from machine import SoftI2C
#from ssd1306 import SSD1306_I2C  #I2C的oled选该方法
from servo import Servo
'''
#创建软件I2C对象
i2c = SoftI2C(sda=Pin(19), scl=Pin(18))
#创建OLED对象，OLED分辨率、I2C接口
oled = SSD1306_I2C(128, 64, i2c)
'''
#LaserPin = 15    # 定义激光传感器管脚为Pin15

#定义SG90舵机控制对象
my_servo1 = Servo(Pin(27))    #下
my_servo2 = Servo(Pin(22))    #上
'''
#定义UART控制对象
uart=UART(2,115200,rx=16,tx=17)
'''
# 定义矩阵键盘的行和列引脚
rows = [Pin(26, Pin.OUT), Pin(25, Pin.OUT), Pin(33, Pin.OUT), Pin(32, Pin.OUT)]
cols = [Pin(4, Pin.IN, Pin.PULL_UP), Pin(14, Pin.IN, Pin.PULL_UP), Pin(5, Pin.IN, Pin.PULL_UP), Pin(23, Pin.IN, Pin.PULL_UP)]

# 定义键盘按键对应的字符
keys = [
    ['left', '1', '2', '3'],
    ['right', '4', '5', '6'],
    ['down', '7', '8', '9'],
    ['up', 'D', '0', 'E']
]

# 读取键盘按键状态
def read_key():
    for i in range(4):
        rows[i].value(0)
        for j in range(4):
            if cols[j].value() == 0:
                time.sleep(0.02)
                rows[i].value(1)
                return keys[i][j]
        rows[i].value(1)
    return None

#中断回调函数
def fun(tim):
    '''
    oled.fill(0)  # 清屏,背景黑色
    oled.show()
    
    if uart.any():                
        print(str(uart.read()))        
        time.sleep(0.1)
        oled.text(str(uart.read(128)),0,30,1)  #显示字符串
        oled.show()  #执行显示
    '''
      
     # 循环读取键盘按键状态
    key = read_key()
    if key is not None:
        print(key)
        #oled.text(str(key),60,0,1)  #显示字符串
        #oled.show()  #执行显示
        '''
        if key=='D':
            Laser.value(1)
        if key=='E':
            Laser.value(0)
        '''
#开启RTOS定时器
tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=fun) #周期1s    

#程序入口
if __name__=="__main__":
    '''
    global Laser
    
    Laser = Pin(LaserPin,Pin.OUT) # 设置Pin模式为输出模式
    Laser.value(0) 
    oled.fill(0)  #清空屏幕
    oled.show()  #执行显示
    '''
    angle1=0
    angle2=0
    
    my_servo1.write_angle(84)   #复位
    my_servo2.write_angle(66)
    
    #my_servo1.write_angle(92)  
    #my_servo2.write_angle(67)
    
    
    while True:
        fun(tim)
        key = read_key()
        
        if key=='left':
            time.sleep(0.1)
            angle1=angle1+5
            my_servo1.write_angle(int(angle1))
            time.sleep(0.5)
            if angle1==180:
                angle1=180
        if key=='right':
            time.sleep(0.1)
            angle1=angle1-5
            my_servo1.write_angle(int(angle1))
            time.sleep(0.5)
            if angle1==0:
                angle1=0
        if key=='down':
            time.sleep(0.1)
            angle2=angle2+5
            my_servo2.write_angle(int(angle2))
            time.sleep(0.5)
            if angle2==180:
                angle2=180
        if key=='up':
            time.sleep(0.1)
            angle2=angle2-5
            my_servo2.write_angle(int(angle2))
            time.sleep(0.5)
            if angle2==0:
                angle2=0
                
                
        if key=='1':
            
            my_servo1.write_angle(100)  #左上1
            my_servo2.write_angle(54)
            time.sleep(1)
            my_servo1.write_angle(82)  #上中
            my_servo2.write_angle(52)
            time.sleep(1)
            my_servo1.write_angle(67)  #右上2
            my_servo2.write_angle(54)
            time.sleep(1)
            my_servo1.write_angle(68)  #右中
            my_servo2.write_angle(65)
            time.sleep(1)
            my_servo1.write_angle(68)  #右下4
            my_servo2.write_angle(81)
            time.sleep(1)
            my_servo1.write_angle(82)  #下中
            my_servo2.write_angle(82)
            time.sleep(1)
            my_servo1.write_angle(98)  #左下3
            my_servo2.write_angle(81)
            time.sleep(1)
            my_servo1.write_angle(99)  #左中
            my_servo2.write_angle(68)
            time.sleep(1)
            
            my_servo1.write_angle(100)  #左上1
            my_servo2.write_angle(54)
            time.sleep(1)
            my_servo1.write_angle(84)  #复位
            my_servo2.write_angle(66)
            time.sleep(1)
        
        if key=='2':
            my_servo1.write_angle(93)  #左上
            my_servo2.write_angle(62)
            time.sleep(1)
            my_servo1.write_angle(85)  
            my_servo2.write_angle(61)
            time.sleep(1)
            my_servo1.write_angle(75)  #右上
            my_servo2.write_angle(61)
            time.sleep(1)
            my_servo1.write_angle(74)  
            my_servo2.write_angle(65)
            time.sleep(1)
            my_servo1.write_angle(76)  #右下
            my_servo2.write_angle(72)
            time.sleep(1)
            my_servo1.write_angle(84)  
            my_servo2.write_angle(72)
            time.sleep(1)
            my_servo1.write_angle(91)  #左下
            my_servo2.write_angle(71)
            time.sleep(1)
            
            my_servo1.write_angle(93)  #左上
            my_servo2.write_angle(62)
            time.sleep(1)
            
            my_servo1.write_angle(84)  #复位
            my_servo2.write_angle(66)
            time.sleep(1)
        '''
        if key=='3':
            my_servo1.write_angle(10)
            time.sleep(0.5)
            my_servo2.write_angle(73)
            time.sleep(0.5)
        if key=='4':
            my_servo1.write_angle(70)
            time.sleep(0.5)
            my_servo2.write_angle(70)
            time.sleep(0.5)
        if key=='5':
            my_servo1.write_angle(30)
            time.sleep(0.5)
            my_servo2.write_angle(75)
            time.sleep(0.5)
        if key=='6':
            my_servo1.write_angle(10)
            time.sleep(0.5)
            my_servo2.write_angle(82)
            time.sleep(0.5)
        if key=='7':
            my_servo1.write_angle(70)
            time.sleep(0.5)
            my_servo2.write_angle(100)
            time.sleep(0.5)
        if key=='8':
            my_servo1.write_angle(30)
            time.sleep(0.5)
            my_servo2.write_angle(100)
            time.sleep(0.5)
        if key=='9':
            my_servo1.write_angle(10)
            time.sleep(0.5)
            my_servo2.write_angle(98)
            time.sleep(0.5)
       '''
        if key=='0':
            my_servo1.write_angle(84)
            my_servo2.write_angle(66)
            time.sleep(0.5)
        
        
            