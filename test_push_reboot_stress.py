#！/usr/bin/env python38
# coding=utf-8

import os,time
import subprocess

def cmd(command):
    subp = subprocess.run(command,shell=True,capture_output=True,encoding="utf-8")
    if subp.stdout:
        print(subp.stdout)
    elif subp.stderr:
        print("失败", subp.stderr)  
    else:
        print(subp)

def mainRunner():
    #while True:
    for i in range(0,3000):
        print("\n第"+str(i+1)+"次测试开始:\n")
        cmd("adb reboot")
        time.sleep(20)
        cmd("adb root")

        print("\nadb remount\n")
        time.sleep(0.05)
        cmd("adb remount")
        time.sleep(5)

        print("\nadb push ./Test_Image/. /sdcard/Pictures\n")
        time.sleep(0.05)
        cmd("adb push ./Test_Image/. /sdcard/Pictures")
        time.sleep(2)

        print("\nadb push ./Test_Music/. /sdcard/Music\n")
        time.sleep(0.05)
        cmd("adb push ./Test_Music/. /sdcard/Music")
        time.sleep(5)

        print("\nadb push ./Test_video/. /sdcard/Movies\n")
        cmd("adb push ./Test_video/. /sdcard/Movies")
        time.sleep(130)

mainRunner()
