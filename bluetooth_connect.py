import uiautomator2 as u2
import time

wait_time = 60

try:
	d=u2.connect()
	d.info
except Exception:
	print("无法连接到设备\n请检查连接")
	exit()

d.app_start("com.android.car.settings", stop=True)
d(text="Settings").wait(timeout=10)
d(text="More").click()
d(scrollable=True).scroll.to(text="Bluetooth")
d(text="Bluetooth").click()
# 蓝牙开
switch = d.xpath('//*[@resource-id="com.android.car.settings:id/toggle_switch"]').rect
d.swipe(switch[0]+switch[2]//3, switch[1]+switch[3]//2, switch[0]+200, switch[1]+switch[3]//2)
if not d(text="Bluetooth will turn on to pair").wait_gone(timeout=60):
	print("蓝牙开启失败")
	exit()

if d(text="Paired devices").exists():
	# 拉个已连接设备的表
	paired = d.xpath('//*[@resource-id="com.android.car.settings:id/nested_recycler_view_layout"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout').all()
	choice = 1
	if len(paired)>2:
		print(f"发现{len(paired)-1}个设备")
		choice = int(input("选择第几个> "))
	# 点进选的设备的设置页
	x_coor = d(resourceId='android:id/widget_frame').center()[0]
	d.click(x_coor,paired[choice].center()[1])
else:
	# d(text="Pair new device").click()
	print("No paired device")
	print("请先手动连接一个设备")
	exit()
# d.xpath('//*[@resource-id="com.android.car.settings:id/nested_recycler_view_layout'
		# '"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2'
		# ']/android.widget.LinearLayout[1]').click()
counter = 1
results = {'ave' : 0, 'max' : 0, 'min' : wait_time}
# 右上角按钮
button = d.xpath('//*[@resource-id="com.android.car.settings:id/action_button1"]')
while 1:
	print("    循环第", counter, "次")
	print(f"平均:{results['ave']:.2f}, 最小:{results['min']:.2f}, 最大:{results['max']:.2f}", end = '\r')

	time.sleep(1)
	time_start = time.time()
	# 如果蓝牙开着，关掉
	if button.text=="Disconnect":
		# 设备名下的连接状态
		stat = d.xpath('//*[@resource-id="android:id/summary"]')
		button.click()
		stat.wait_gone()

	# 开蓝牙
	button.click()
	if d(text="Disconnect").wait(timeout=10):
		# if d.xpath('//*[@resource-id="android:id/summary"]').text != "Connected":
		if not d(text='Connected').wait(timeout=wait_time):
			element_text = d.xpath('//*[@resource-id="android:id/summary"]').text
			print(f'\n\n连接时间超过{wait_time}秒!!\n连接异常状态为"{element_text}"')
			break
		# 连上设备
		time_cost = time.time() - time_start
	else:
		print(f'\n\n尝试连接失败,检查connect按钮是否失效')
		break

	if time_cost > results['max']:
		results['max'] = time_cost
	if time_cost < results['min']:
		results['min'] = time_cost
	results['ave'] = results['ave'] - results['ave']/counter + time_cost/counter
	print(f"\x1b[K      花费{time_cost:.2f}秒\n")

	counter += 1

raise TimeoutError
