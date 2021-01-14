# coding: utf-8

import uiautomator2 as u2
import time
from time import sleep
import logging

#config logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
sleep(5)

d=u2.connect()
sleep(5)

#Enter all apps
d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
sleep(2)
#start_map
d(resourceId="com.android.car.carlauncher:id/app_name", text="Amap Auto").click()
sleep(5)
d.click(79,310)
sleep(2)
    
def routeMap1():
    d.click(1278,412)
    sleep(2)
    d.click(166,249)
    sleep(1) 
    
def routeMap2():
    d.click(1278,412)
    sleep(2)
    d.click(182,370)
    sleep(1)     

def routeMap3():
    d.click(1278,412)
    sleep(2)
    d.click(128,462)
    sleep(1)  
    
def runMap():
    d.click(577,172)
    sleep(2)   
    d.click(513,60)
    sleep(200)
    d.click(779,220)
    sleep(2)  
    d.click(65,559)
    sleep(3)
    d.click(50,568)
    sleep(3)
                
if __name__=='__main__':
    while True:
    #for i in range(1,5):
        routeMap1()
        runMap()
        routeMap2()
        runMap()
        routeMap3()
        runMap()
        
