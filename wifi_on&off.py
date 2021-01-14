import uiautomator2 as u2
import time

SSID = "Semidrive"
password = "M122122122Z"

try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	raise ConnectionError
	
d.app_start("com.android.car.settings", stop=True)
d(text="Settings").wait(timeout=10)
d(text="More").click()
d(scrollable=True).scroll.to(text="Network & internet")
d(text="Network & internet").click()
d(text="Wi‑Fi").click()

counter = 1
print("开始WiFi启停测试")

switch = d.xpath('//*[@resource-id="com.android.car.settings:id/toggle_switch"]').rect

while 1:
	print("循环第", counter, "次")
	counter += 1

	try:
		# off
		d.swipe(switch[0]+switch[2]//3*2, switch[1]+switch[3]//2, switch[0]-100, switch[1]+switch[3]//2)
		time.sleep(0.5)
		# on
		d.swipe(switch[0]+switch[2]//3, switch[1]+switch[3]//2, switch[0]+200, switch[1]+switch[3]//2)
		time.sleep(1)
		time_start = time.time()
	except Exception:
		print("人为操作打断")
		break

	if not d(text=SSID).click_exists(timeout=3):
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

	print(f'   {time.time()-time_start:.2f} seconds')