import uiautomator2 as u2
import time

SSID = "Semidrive"
passwork = "M122122122Z"

try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	exit()
d.app_start("com.android.car.settings", stop=True)
d(text="Settings").wait(timeout=10)
d.long_click(400,400,1)
counter = 1
print("开始WiFi启停测试")

while 1:
	print("循环第", counter, "次")
	counter += 1

	try:
		d.swipe(1840,115,1700,115,0.05)
		time.sleep(0.5)
		d.swipe(1800,115,1900,115,0.05)
		time.sleep(1)
	except Exception:
		print("人为操作打断")
		break

	if d(text=SSID).wait(timeout=3):
		d(text=SSID).click()
	else:
		print("未检测到WiFi")
		break

	if d(text="Forget").wait(timeout=1):
		d.press("back")

	if d(text="Show password").exists():
		d.send_keys(password)
		d(text="OK").click()
		
	if not (d(text="Connected, no internet").wait(timeout=5) or d(text="Limited connection").exists()):
		print("Connection failed")
		break