#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 本程序以三星s7手机为例，屏幕分辨率1080*1920
# 使用的是绝对坐标，分辨率相同的安卓手机可以直接使用，其他分辨率手机需要手动修改坐标
# 仅限安卓，iphone不适用
# 使用前请先安装adb，然后进去淘宝的“618理想大赢家”界面

import os
import time
from PIL import Image
def screencap():
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    img = Image.open('screen.png')
    print(img.getpixel((1167, 1751)))
    print(img.getpixel((1200, 1007)))

def qu_guang_dian():
    print('====== 进入领喵币中心,去逛店 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 1204 2278')  # 点击领喵币
    for i in range(1, 20):
        print('第{}次去逛店...'.format(i))
        time.sleep(1)
        os.system('adb shell input tap 1170 1476')  # 点击去逛店，然后等15s
        print('进入店铺,浏览页面中，请等待15s...')
        time.sleep(25)
        os.system('adb shell input keyevent KEYCODE_BACK')
    print('已完成去逛店领取喵币任务')
    os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
def liu_lan_hui_chang():
    print('====== 进入领喵币中心，浏览会场 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 1204 2278')  # 点击下方领喵币
    for i in range(1, 5):
        print('第{}次去浏览会场...'.format(i))
        time.sleep(3)
        os.system('adb shell input tap 1189 1730')  # 点击去会场
        print('浏览会场中，请等待15s...')
        time.sleep(17)
        os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
    print('已完成浏览会场领取喵币任务')
    os.system('adb shell input tap 996 136')  # 点击右上角关闭


#qu_guang_dian()
liu_lan_hui_chang()
screencap()