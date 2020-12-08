import uiautomator2 as u2
import time
try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	exit()
d.app_start("com.google.android.car.kitchensink", stop=True)
d(text="BLUETOOTH HEADSET").click()
d(text="PICK DEVICE").click()
if not d(text="Connected").click_exists(timeout=5):
	print("Connect a device manually first!")
d(text="Enter number").click()
d.send_keys("10000")
d(text="START CALL").click()
