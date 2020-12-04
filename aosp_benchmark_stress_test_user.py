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



def antutuTest():
    #Enter all apps
    d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(2)    
    d(scrollable=True).scroll.to(text="AnTuTu Benchmark")
    sleep(1)
    d(resourceId="com.android.car.carlauncher:id/app_name", text="AnTuTu Benchmark").click()
    sleep(5)
    for i in range(0,5):
        d(scrollable=True).scroll.to(text="Test Again")
        sleep(1)
        d(text="Test Again").click()
        sleep(900)
        d.screenshot("D:\Test_log\screen_shot"+"_"+"antutu"+str(i+1)+"screenshot.jpg")
        sleep(3)
        d.press("back")
        sleep(1)
        
        
def aibenchTest():
    #Enter all apps
    d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(2)    
    d(scrollable=True).scroll.to(text="AI Benchmark")
    sleep(1)
    d(resourceId="com.android.car.carlauncher:id/app_name", text="AI Benchmark").click()
    sleep(5)
    #d(resourceId="org.benchmark.demo:id/circleView").click()
    #sleep(900)
    for i in range(0,5):
        d(resourceId="org.benchmark.demo:id/restartButton").click()
        sleep(900)
        d.screenshot("D:\Test_log\screen_shot"+"_"+"AIBenchmark"+str(i+1)+"screenshot.jpg")
        sleep(3)

#run Ludashi
def aimarkTest():
    #Enter all apps
    d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(2)    
    d(scrollable=True).scroll.to(text="AImark")
    sleep(1)
    d(resourceId="com.android.car.carlauncher:id/app_name", text="AImark").click()
    sleep(5)
    #d(resourceId="com.ludashi.aibench:id/bench").click()
    #sleep(1)
    #d(resourceId="com.ludashi.aibench:id/btn_right").click()
    #sleep(900)
    for i in range(0,5):
        d(resourceId="com.ludashi.aibench:id/reBench").click()
        sleep(900)
        d.screenshot("D:\Test_log\screen_shot"+"_"+"AImark"+str(i+1)+"screenshot.jpg")
        sleep(3)
        
#run androbench
def androTest():
    #Enter all apps
    d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(2)    
    d(scrollable=True).scroll.to(text="AndroBench")
    sleep(1)
    d(resourceId="com.android.car.carlauncher:id/app_name", text="AndroBench").click()
    sleep(5)
    #d(resourceId="com.android.car.carlauncher:id/app_name", text="AndroBench").click()
    #sleep(1)
    #d(resourceId="com.andromeda.androbench2:id/btnStartingBenchmarking").click()
    #sleep(1)
    #d(resourceId="android:id/button1").click()
    #sleep(300)
    for i in range(0,5):
        d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.LinearLayout[1]').click()
        sleep(1)
        d(resourceId="com.andromeda.androbench2:id/btnStartingBenchmarking").click()
        sleep(1)
        d(resourceId="android:id/button1").click()
        sleep(300)
        d(resourceId="android:id/button1").click()
        sleep(1)
        d.screenshot("D:\Test_log\screen_shot"+"_"+"AndroBench"+str(i+1)+"screenshot.jpg")
        sleep(3)

#run GeekBench5        
def geekTest():
    #Enter all apps
    d.xpath('//*[@resource-id="com.android.systemui:id/grid_nav"]/android.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
    sleep(2)    
    d(scrollable=True).scroll.to(text="Geekbench 5")
    sleep(1)
    d(resourceId="com.android.car.carlauncher:id/app_name", text="Geekbench 5").click()
    sleep(5)
    for i in range(0,5):
        d.xpath('//*[@resource-id="com.primatelabs.geekbench5c:id/tabLayout"]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar-Tab[1]').click()
        sleep(1)
        d(resourceId="com.primatelabs.geekbench5c:id/runCpuBenchmarks").click()
        sleep(900)
        d.screenshot("D:\Test_log\screen_shot"+"_"+"geekbench"+"_"+"cpu"+str(i+1)+"screenshot.jpg")
        sleep(1)
        d.press("back")
        d.xpath('//*[@resource-id="com.primatelabs.geekbench5c:id/tabLayout"]/android.widget.LinearLayout[1]/android.support.v7.app.ActionBar-Tab[2]').click()
        sleep(1)
        d(resourceId="com.primatelabs.geekbench5c:id/runComputeBenchmark").click()
        sleep(1800)
        d.screenshot("D:\Test_log\screen_shot"+"_"+"geekbench"+"_"+"gpu"+str(i+1)+"screenshot.jpg")
        sleep(1)
        d.press("back")
        
        
if __name__=='__main__':
    antutuTest()
    sleep(5)
    aibenchTest()
    sleep(5)
    aimarkTest()
    sleep(5)
    androTest()
    sleep(5)
    geekTest()
    sleep(2)
    print("The benchmark test is over!!!!")
        
 
 
 
 
 
 