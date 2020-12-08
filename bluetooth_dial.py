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

if app in d.shell("pm list packages").output:
	d.app_start(app, stop=True)
else:
	if subprocess.run("adb install ./EmbeddedKitchenSinkApp.apk",shell=True).returncode == 0:
		d.app_start(app, stop=True)
	else:
		print("unknown error")
		exit()

d(text="BLUETOOTH HEADSET").click()
d(text="PICK DEVICE").click()
if not d(text="Connected").click_exists(timeout=5):
	print("Connect a device manually first!")
	d.press("back")
d(text="Enter number").click()
d.send_keys("10000")
d(text="START CALL").click()
time.sleep(5)
d(text="END CALL").click()