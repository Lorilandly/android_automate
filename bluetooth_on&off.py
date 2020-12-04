import uiautomator2 as u2
import time
try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	exit()

choice = input("选择测试方式：\n\t1.Settings页面开关蓝牙\n\t2.蓝牙页面开关蓝牙\n"
	"\t3.从电话进入蓝牙\n> ")
try:
	choice = int(choice)
except ValueError:
	print("给个数字呀")
	exit()
if not choice in {1,2,3}:
	print("别闹，输入1,2或者3")
	exit()

if not choice == 3:
	d.app_start("com.android.car.settings", stop=True)
	d(text="Settings").wait(timeout=10)
	d(text="More").click()
	d(scrollable=True).scroll.to(text="Bluetooth")
	d(text="Bluetooth").click()

counter = 1

while 1:
	print("循环第", counter, "次")
	counter += 1

	if choice==3:
		d.app_start("com.android.car.dialer", stop=True)
		if not d(text="Connect to Bluetooth").click_exists(timeout=10):
			print("似乎已连上蓝牙电话\n请断开后重试")

	try:
		time.sleep(0.5)
		d.swipe(1840,115,1700,115,0.05)
		time_start = time.time()
		if choice == 2:
			d.press("back")
			d.press("back")
			d(text="Bluetooth").click()
			time.sleep(0.5)
			d(text="More").click()
			d(scrollable=True).scroll.to(text="Bluetooth")
			d(text="Bluetooth").click()
			time.sleep(0.5)
		else:
			time.sleep(0.5)
			d.swipe(1800,115,1900,115,0.05)
	except Exception:
		print("人为操作打断")
		break

	if d(text="Bluetooth will turn on to pair").wait_gone(timeout=60):
		d(text="Pair new device").click()
		if d(text="Vehicle name").wait(timeout=5):
			time_end = time.time()
			d.press("back")
		else:
			break
	else:
		break
	print(f"  花费{time_end-time_start:.2f}秒\n")

print("蓝牙开启超时!")
