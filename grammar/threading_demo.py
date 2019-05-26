# -*- coding: utf-8 -*-
# author:xls
"""
    threading模块实现多线程
"""
import threading
import time

# demo1
# class MyThread(threading.Thread):
#
#     def run(self):
#         print("%s is running..." % threading.current_thread())
#
# if __name__ == '__main__':
#     for i in range(10):
#         MyThread().start()
# ============================

# demo2
# def show(arg):
#     time.sleep(1)
#     print('thread '+str(arg)+" running....")
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=show, args=(i,))
#         t.start()
# ============================

# demo3
# number = 0
# lock = threading.Lock()   #生成一个互斥锁对象
# def plus(lk):
#     global number       # global声明此处的number是外面的全局变量number
#     lk.acquire()        # 开始加锁
#     for _ in range(1000000):    # 进行一个大数级别的循环加一运算
#         number += 1
#     print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
#     lk.release()        # 释放锁
#
# for i in range(2):      # 用2个子线程，就可以观察到脏数据
#     t = threading.Thread(target=plus,args=(lock,))
#     t.start()
# time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
# print("主线程执行完毕后，number = ", number)
# ============================

#利用Event类模拟红绿灯
import threading
import time

event = threading.Event()

def lighter():
    green_time = 5       # 绿灯时间
    red_time = 5         # 红灯时间
    event.set()          # 初始设为绿灯
    while True:
        print("\33[32;0m 绿灯亮...\033[0m")
        time.sleep(green_time)
        event.clear()
        print("\33[31;0m 红灯亮...\033[0m")
        time.sleep(red_time)
        event.set()

def run(name):
    while True:
        if event.is_set():      # 判断当前是否"放行"状态
            print("一辆[%s] 呼啸开过..." % name)
            time.sleep(1)
        else:
            print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
            event.wait()
            print("[%s] 看到绿灯亮了，瞬间飞起....." % name)

if __name__ == '__main__':

    light = threading.Thread(target=lighter,)
    light.start()

    for name in ['奔驰', '宝马', '奥迪']:
        car = threading.Thread(target=run, args=(name,))
        car.start()
