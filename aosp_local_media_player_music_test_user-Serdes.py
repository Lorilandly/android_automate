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
#start_Local Media Player
d(resourceId="com.android.car.carlauncher:id/app_name", text="Local Media Player").click()
sleep(5)

#enter music file_start
d.click(1150,480)
sleep(2)
d.click(1130,450)
sleep(1)
#for i in range(1,3):
while True:
    i=0
    j=0
    k=0
    for i in range(1,100):
    #play_pause_stop
        d.click(960,540)
        sleep(0.5)
    
    for j in range(1,200):
    #skip_prev
        d.click(730,556)
        sleep(0.5)
    
    for k in range(1,100):
    #skip_next
        d.click(1190,550)
        sleep(0.5)