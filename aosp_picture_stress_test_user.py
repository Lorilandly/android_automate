# coding: utf-8

import uiautomator2 as u2
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
sleep(1)

#start_Gallery
d(scrollable=True).scroll.to(text="Gallery")
d(resourceId="com.android.car.carlauncher:id/app_name", text="Gallery").click()
sleep(3)

d.click(935,455)
sleep(2)

d.click(134,179)
sleep(2)

#for i in range(1,10):
while True:
    for i in range(1,23):
        d.swipe(1129,302,294,437)
        sleep(0.05)
    for j in range(1,23):
        d.swipe(204,287,943,405)
        sleep(0.05)