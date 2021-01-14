import uiautomator2 as u2
import time
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
# 右上角按钮
button = d.xpath('//*[@resource-id="com.android.car.settings:id/action_button1"]')
while 1:
	print("循环第", counter, "次")
	counter += 1

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
	if d(text="Connected").wait(timeout=30):
		if d.xpath('//*[@resource-id="android:id/summary"]').text != "Connected":
			break
		# 连上设备
		time_end = time.time()
	else:
		break
	print(f"  花费{time_end-time_start:.2f}秒\n")

print("连接失败!")
