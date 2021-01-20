import uiautomator2 as u2
import time

wait_time = 60

# 连接设备
try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	raise ConnectionError

choice = input("选择测试方式：\n\t1.蓝牙页面开关蓝牙\n\t2.Settings页面开关蓝牙\n"
	"\t3.从电话进入蓝牙\n> ")
try:
	choice = int(choice)
except ValueError:
	print("给个数字呀")
	exit()
if not choice in {1,2,3}:
	print("别闹，输入1,2或者3")
	exit()

# 进入安卓设置蓝牙页
if not choice == 3:
	d.app_start("com.android.car.settings", stop=True)
	d(text="Settings").wait(timeout=10)
	d(text="More").click()
	d(scrollable=True).scroll.to(text="Bluetooth")
	d(text="Bluetooth").click()

results = {'ave' : 0, 'max' : 0, 'min' : wait_time}
counter = 1

while 1:
	print("    循环第", counter, "次")
	print(f"平均:{results['ave']:.2f}, 最小:{results['min']:.2f}, 最大:{results['max']:.2f}", end = '\r')

	# 从电话进入蓝牙
	if choice==3:
		d.app_start("com.android.car.dialer", stop=True)
		if not d(text="Connect to Bluetooth").click_exists(timeout=3):
			print("似乎已连上蓝牙电话\n请断开后重试")
			exit()

	try:
		time.sleep(0.5)
		# 蓝牙开关坐标
		switch = d.xpath('//*[@resource-id="com.android.car.settings:id/toggle_switch"]').rect
		# 关
		d.swipe(switch[0]+switch[2]//3*2, switch[1]+switch[3]//2, switch[0]-100, switch[1]+switch[3]//2)

		if not d(text='Bluetooth will turn on to pair').wait(timeout=3):
			print('Error')
			exit()
		time_start = time.time()
		if choice == 2:
			# 回到主页，点击蓝牙开关，回到蓝牙页
			d.press("back")
			d.press("back")
			# bluetooth icon
			d.xpath('//*[@resource-id="com.android.car.settings:id/nested_recycler_view_layout"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2]').click()
			time.sleep(0.5)
			d(text="More").click()
			d(scrollable=True).scroll.to(text="Bluetooth")
			d(text="Bluetooth").click()
			time.sleep(0.5)
		else:
			# 直接开蓝牙
			time.sleep(0.5)
			d.swipe(switch[0]+switch[2]//3, switch[1]+switch[3]//2, switch[0]+200, switch[1]+switch[3]//2)
	except Exception:
		print("人为操作打断")
		break

	if d(text="Bluetooth will turn on to pair").wait_gone(timeout=wait_time):
		d(text="Pair new device").click()
		if d(text="Vehicle name").wait(timeout=5):
			# 蓝牙开启成功
			time_cost = time.time()-time_start
			d.press("back")
		else:
			break
	else:
		break
	if time_cost > results['max']:
		results['max'] = time_cost
	if time_cost < results['min']:
		results['min'] = time_cost
	results['ave'] = results['ave'] - results['ave']/counter + time_cost/counter
	print(f"\x1b[2K      花费{time_cost:.2f}秒\n")
	counter += 1

print("蓝牙开启超时!")
