# coding: utf-8

import uiautomator2 as u2
from time import sleep
import logging

#config logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
sleep(5)

d=u2.connect_usb('0123459876')
sleep(5)

#Enter all apps
d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
sleep(2)
#start_Gallery
d(scrollable=True).scroll.to(text="Gallery")
sleep(1)
d(resourceId="com.android.car.carlauncher:id/app_name", text="Gallery").click()
sleep(5)

#enter movie file
d.click(935,183)
sleep(2)

#for i in range(1,3):
while True:
#start test
    d.click(134,204)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)

    d.click(427,196)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)

    d.click(715,198)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(1002,198)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(1280,198)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(1555,198)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)    

    d.click(143,483)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5) 
    
    d.click(427,483)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(712,483)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(997,483)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(1291,483)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)
    
    d.click(1568,483)
    sleep(1)
    d.click(962,315)
    sleep(1)
    for i in range(1,100):
        d.click(641,385)
        sleep(1)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(0.5)