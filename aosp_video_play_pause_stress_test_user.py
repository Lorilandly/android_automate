# coding: utf-8

import uiautomator2 as u2
from time import sleep
import logging

#config logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

d=u2.connect()
disp = d.info
X = disp['displaySizeDpX']
Y = disp['displaySizeDpY']

# enter gallery
d.app_start("com.android.gallery3d", stop=True)
d(text='Albums').wait()

#enter movie file
d.click(0.5*X,0.3*Y)
d(text='Movies').wait()

#for i in range(1,3):
while True:
    # press on video
    d.click(0.4*X,0.3*Y)
    sleep(1)
    for i in range(10):
        for j in range(20):
            d.click(0.4*X,0.4*Y)
        d.click(0.5*X,0.4*Y)
        sleep(10)
        for j in range(20):
            d.click(0.4*X,0.4*Y)
        d.press('back')
        sleep(1)
        d.swipe(0.9*X,0.5*Y,0,0.5*Y)
        sleep(1)
    d.press('back')
    sleep(1)
    continue
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