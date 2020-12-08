import uiautomator2 as u2
import subprocess
import time
app = "com.google.android.car.kitchensink"

try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	exit()

if not app in d.shell("pm list packages").output:
	if not subprocess.run("adb install ./EmbeddedKitchenSinkApp.apk",shell=True).returncode == 0:
		print("unknown error")
		exit()

d.app_start("com.android.car.settings", stop=True)
d(text="Settings").wait(timeout=10)
d(text="More").click()
d(scrollable=True).scroll.to(text="Bluetooth")
d(text="Bluetooth").click()
# 蓝牙开
d.swipe(1800,115,1900,115,0.05)
if not d(text="Bluetooth will turn on to pair").wait_gone(timeout=60):
	print("蓝牙开启失败")
	exit()

if d(text="Paired devices").exists():
	if not d(text="Connected").exists:
		# 拉个已连接设备的表
		paired = d.xpath('//*[@resource-id="com.android.car.settings:id/nested_recycler_view_layout"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout').all()
		choice = 1
		if len(paired)>2:
			print(f"发现{len(paired)-1}个设备")
			choice = int(input("选择第几个> "))
		# 点击连接设备
		paired[choice].click()
		if not d(text="Connected").wait(timeout=30):
			print("Error connecting")
			exit()
else:
	# d(text="Pair new device").click()
	print("No paired device")
	print("请先手动连接一个设备")
	exit()

d.app_start(app, stop=True)
d(text="BLUETOOTH HEADSET").click()
d(text="PICK DEVICE").click()
d(text="Connected").click_exists(timeout=3)
d(text="Enter number").click()
d.send_keys("10000")
d(text="START CALL").click()
time.sleep(5)
d(text="END CALL").click()
