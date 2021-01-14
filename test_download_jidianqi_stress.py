#！ python38
# coding=utf-8
import uiautomator2 as u2
import time
from time import sleep
import logging

exit_all = False
def usage():
     print("Usage: optcode  test_count delay_time")
     print("       optcode: 0 - power off, no need for test_count and delay_time")
     print("                1 - power on, no need for test_count and delay_time")
     print("                2- reset x9_evb board and check if android boot sucessfully")
     
def get_os_type():
    #获取操作系统类型，Linux or Windows
    return platform.system()

def serial_opt(ser,opt, delay):
    opt_v=[]
    onrelay=(0xAA,0x00)
    offrelay=(0xBB,0x00)
    #onrelay=(0xaa,0)
    #offrelay=(0xbb, 0) 
    if opt==0:
        opt_v=offrelay
        print("下电", end="")
    else:
        opt_v=onrelay
        print("上电",end="")

    result=ser.write(opt_v)    
    if result != 2:
        print("失败"+str(result))
    else:
        print("成功")
    time.sleep(delay)
                
def init_power_serial():
    DEFUALT_COM_DES = "USB-SERIAL CH340"        
    portx=""  
    bps=9600
    timex=5

    plist = list(serial.tools.list_ports.comports())
    #print("plist:"+str(len(plist)))

    for port in plist:       
        #if port.description.find(DEFUALT_COM_DES) >= 0:
        if port.vid == 0x1a86 and port.pid == 0x7523:
            portx = port.name
            print(port.description)
        
    ser=serial.Serial(portx, bps, timeout=timex)             
    print("\nprot:"+str(portx)+" baud:"+str(bps))
    return ser

def deinit_power_serial(ser):
    ser.close()#关闭串口
    
def deinit_log_serial(ap_ser):
    ap_ser.close()#关闭串口

def get_current_time():
    curr_time = datetime.datetime.now()    
    file_time = curr_time.strftime("_%m%d%H%M")     #保留月日小时分钟
    return file_time
    
def save_fail_log():
    log_time = get_current_time()
    adb_root = 'adb root'
    adb_remount = 'adb remount'
    log_path = "D:\\Android_log" + log_time
    rm_log_cmd = 'adb shell rm -rf /data/sdrv_logs'
    if os.path.exists(log_path) == False:
        os.mkdir(log_path)
    adb_pull = 'adb pull /data/sdrv_logs ' + log_path
    os.popen(adb_root)    
    time.sleep(3)
    os.popen(adb_remount)    
    time.sleep(3)
    ret_pull = os.popen(adb_pull)   
    ret_str = ret_pull.read()
    if ret_str.find("error") != -1:
        print("adb pull /data/sdrv_logs folder FAIL!!!")
    time.sleep(1)
    os.popen(rm_log_cmd)    
    time.sleep(1)
    
    
def clean_sdrv_logs():
    adb_root = 'adb root'
    adb_remount = 'adb remount'
    rm_log_cmd = 'adb shell rm -rf /data/sdrv_logs'
    os.popen(adb_root)    
    time.sleep(3)
    os.popen(adb_remount)    
    time.sleep(3)
    os.popen(rm_log_cmd)    
    time.sleep(1)
       

def get_boot_status(timeout):
    print("Start to check Android boot status")
    adb_getprop = 'adb shell getprop sys.boot_completed'
    for i in range(0, timeout):
        d = os.popen(adb_getprop)
        f = d.read()
        if f.strip() == "1":
            #print("getprop sys.boot_completed = " + f.strip())
            break
        print("getprop sys.boot_completed = " + f.strip())            
        time.sleep(1)
    print("getprop sys.boot_completed = " + f.strip())
    if i == (timeout - 1):
        print("getprop sys.boot_completed timeout, Android boot fail")
        #save_fail_log()
        return 0
    else:
        print("Android boot OK")
        clean_sdrv_logs()
        return 1
    print("check Android boot status finished")
    
def init_ap_serial():
    portx=""  
    bps=115200
    timex=1

    plist = list(serial.tools.list_ports.comports())
    #print("plist:"+str(len(plist)))
    port_ap_log=""
    port_min=""
    log_port_list=[]
    for port in plist:       
        #if port.description.find(DEFUALT_COM_DES) >= 0:
        if port.vid == 0x0403 and port.pid == 0x6011:
            log_port_list.append(port)
    
    log_port_list.sort()
    port_ap_log = log_port_list[2].name
    ap_ser=serial.Serial(port_ap_log,bps,timeout=timex)     
    print("\nap core debug com:"+str(port_ap_log))
  
    return ap_ser
    
def read_log(ser, tofile, filename):
    global exit_all
    if tofile == True:
        f = open(filename, 'w',encoding='utf-8')

    while True:
        if exit_all == True:
            print("read_log will exit")
            break
        #str = ser.readline().decode(encoding='UTF-8',errors='ignore')
        str = (ser.readline().decode(encoding='UTF-8')).strip("\n")
        if len(str) > 0:
            f.write(str)
        #print(str)      
    if tofile == True:
        f.close()
        
def save_ap_log():
    print("Start to save ap log")
    ap_ser = init_ap_serial()   
    log_time = get_current_time()
    save_log_path = "D:\\ap_log" + log_time + ".txt"
    thread_ap = threading.Thread(target=read_log, name="ap-core", args=(ap_ser, True, save_log_path))
    thread_ap.start()
    return ap_ser    

def start_android_autolog():
    print("start to save android log automatic")
    adb_root = 'adb root'
    adb_remount = 'adb remount'
    adb_autolog = 'adb shell setprop persist.log.start 1'
    adb_rm_log = 'adb shell rm -rf /data/sdrv_logs'
    serial_opt(ser,1,30)     #上电30s，保证adb可用
    os.popen(adb_root)    
    time.sleep(1)
    os.popen(adb_remount)
    time.sleep(1)
    os.popen(adb_autolog)
    time.sleep(1)
    serial_opt(ser,0,5)    #断电重启
    
    serial_opt(ser,1,30)     #上电30s，保证adb可用
    os.popen(adb_root)    
    time.sleep(1)
    os.popen(adb_remount)
    time.sleep(1)
    os.popen(adb_rm_log)    #测试前需先删除sdrv_logs文件夹
    time.sleep(1)
    serial_opt(ser,0,5)
    print("set android log automatic finished")
    

def stop_android_autolog():
    adb_root = 'adb root'
    adb_remount = 'adb remount'
    adb_autolog_stop = 'adb shell setprop persist.log.start 0'   
    os.popen(adb_root)    
    time.sleep(3)
    os.popen(adb_remount)
    time.sleep(3)
    os.popen(adb_autolog_stop)


    
def reset_x9_evb_boot(ser,count):
    global exit_all
    timeout = 100
    serial_opt(ser,0,5)
    ap_ser = save_ap_log()    #测试中一直保存ap串口log
    start_android_autolog()
    for num in range(0,count):
        print("\n第"+str(num+1)+"次测试开始:\n")
        serial_opt(ser,1,5)
        ret = get_boot_status(timeout)  
        if ret == 0:
            break
        time.sleep(3)        
        serial_opt(ser,0,5)       
        print("\n第"+str(num+1)+"次测试完成\n")
    
    exit_all = True
    deinit_log_serial(ap_ser)
    stop_android_autolog()

    
if __name__=="__main__":
    if len(sys.argv) == 1:
        usage();
        exit();        
        
    test_case = sys.argv[1]
    count = 1
    delay = 20
    if len(sys.argv) >=3:
            count = int(sys.argv[2])
            
    if len(sys.argv) >= 4:
            delay = int(sys.argv[3])
            
    ser = init_power_serial()
    if test_case == "0":
        serial_opt(ser, 0,0)
    elif test_case == "1":
        serial_opt(ser, 1,0)
    elif test_case == "2":
        reset_x9_evb_boot(ser,count)
    else:
        usage()
    
    deinit_power_serial(ser)
    os._exit(0)




