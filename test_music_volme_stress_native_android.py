# coding: utf-8

import uiautomator2 as u2
from time import sleep
import logging
import random

#config logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
sleep(5)

d=u2.connect()
sleep(5)

def playMusic():
    #Enter all apps
    d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(2)
    #start_Local Media Player
    d(scrollable=True).scroll.to(text="Local Media Player")
    sleep(1)
    d(resourceId="com.android.car.carlauncher:id/app_name", text="Local Media Player").click()
    sleep(5)
    #enter music file_start
    d(resourceId="com.android.car.media:id/title", text="Music").click()
    sleep(2)
    d(resourceId='com.android.car.media:id/thumbnail').click()
    sleep(1)
    for j in range(1,3):
        for i in range(50):
            #play_pause_stop
            d(resourceId='com.android.car.media:id/play_pause_stop').click()
            sleep(0.5)
        for i in range(50):
            #skip_prev
            d(resourceId='com.android.car.media:id/skip_prev').click()
            sleep(0.5)
        for i in range(50):
            #skip_next
            d(resourceId='com.android.car.media:id/skip_next').click()
            sleep(0.5)
    d.press("back")
    
                
def adjustVolme():
    d.app_start("com.android.car.settings", stop=True)
    d(text="Settings").wait(timeout=10)
    d(text="More").click()
    d(scrollable=True).scroll.to(text="Sound")
    d(text="Sound").click()

    volume0 = d.xpath(
        '//*[@resource-id="com.android.car.settings:id/nested_recycler_view_layout"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
        ).rect
    volume1 = d.xpath(
        '//*[@resource-id="com.android.car.settings:id/nested_recycler_view_layout"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
        ).rect
    
    #adjut media volume0 and volume1
    for j in range(1,100):
        for i in range(30):
            # 随机点
            d.click(random.randint(volume0[0], volume0[0]+volume0[2]), volume0[1]+volume0[3]/2)
            sleep(10)
        for i in range(30):
            # 随机点
            d.click(random.randint(volume1[0], volume1[0]+volume1[2]), volume1[1]+volume1[3]/2)
            sleep(10)

if __name__=='__main__':
    while True:
    #for i in range(1,3):
        playMusic()
        sleep(5)
        adjustVolme()
        sleep(5)