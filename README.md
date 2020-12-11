# 安卓自动化测试脚本
##运行环境：
- 
- Python3: 配置环境变量
- Adb: 配置环境变量
- Python UIAutomator2: 命令行输入：`python3 -m pip3 install -U uiautomator2` 安装

##运行脚本：
###Bluetooth_on&off.py
该脚本循环测试蓝牙开关功能。
命令行进入脚本目录，输入`python3 Bluetooth_on&off.py`运行
###Bluetooth_connect.py
该脚本循环测试蓝牙连接功能
运行前保证主板与蓝牙设备配对成功，且设备在蓝牙范围内
命令行输入`python3 Bluetooth_connect.py`运行
###Bluetooth_dial.py
该脚本循环测试蓝牙电话功能
运行前保证主板与手机蓝牙配对成功，且手机在蓝牙范围内
命令行输入`python3 Bluetooth_dial.py`运行
默认向电信（10000）打电话。可修改脚本开头的number变量向其他号码打电话