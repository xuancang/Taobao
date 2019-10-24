# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 本程序以三星s7手机为例，屏幕分辨率1080*1920
# 使用的是绝对坐标，分辨率相同的安卓手机可以直接使用，其他分辨率手机需要手动修改坐标
# 仅限安卓，iphone不适用
# 使用前请先安装adb，然后进去淘宝的“618理想大赢家”界面

import os
import time
from PIL import Image
f1=1
f2=1
f3=1
def screencap():
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 1204 2278')
    time.sleep(3)
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    img = Image.open('screen.png')
    print(img.getpixel((1275,1507)))
    if img.getpixel((1275,1507))==(174, 151, 147, 255):
        f1=0
        print(f1)
    print(img.getpixel((1279,1775)))
    if img.getpixel((1279,1775)) == (174, 151, 147, 255):
        f2 = 0
        print(f2)
    if img.getpixel((1289, 1992)) == (174, 151, 147, 255):
        f3 = 0
        print(f3)
    os.system('adb shell input tap 1337 538')

def qu_guang_dian():
    print('====== 进入领喵币中心,去逛店 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 1204 2278')  # 点击领喵币
    i=0
    do=1
    time.sleep(3)
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    img = Image.open('screen.png')
    print(img.getpixel((1275, 1507)))
    if img.getpixel((1275, 1507)) == (174, 151, 147, 255):
        do = 0
    while do:
        os.system('adb shell screencap -p /sdcard/screen.png')
        os.system('adb pull /sdcard/screen.png')
        img = Image.open('screen.png')
        print(img.getpixel((1275, 1507)))
        i=i+1
        if img.getpixel((1275,1507))==(174, 151, 147, 255):
            do=0
        print('第{}次去逛店...'.format(i))
        time.sleep(1)
        os.system('adb shell input tap 1170 1476')  # 点击去逛店，然后等15s
        print('进入店铺,浏览页面中，请等待15s...')
        time.sleep(25)
        os.system('adb shell input keyevent KEYCODE_BACK')
    print('已完成去逛店领取喵币任务')
    os.system('adb shell input tap 1337 538')
    #os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
def liu_lan_hui_chang():
    print('====== 进入领喵币中心，浏览会场 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 1204 2278')  # 点击下方领喵币
    time.sleep(3)
    i = 0
    do=1
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    img = Image.open('screen.png')
    print(img.getpixel((1279, 1775)))
    if img.getpixel((1279, 1775)) == (174, 151, 147, 255):
        do = 0
    while do:
        os.system('adb shell screencap -p /sdcard/screen.png')
        os.system('adb pull /sdcard/screen.png')
        img = Image.open('screen.png')
        print(img.getpixel((1279, 1775)))
        i = i + 1
        if img.getpixel((1279, 1775)) == (174, 151, 147, 255):
            do = 0
        print('第{}次去浏览会场...'.format(i))
        time.sleep(3)
        os.system('adb shell input tap 1189 1730')  # 点击去会场
        print('浏览会场中，请等待15s...')
        time.sleep(17)
        os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
    print('已完成浏览会场领取喵币任务')
    os.system('adb shell input tap 1337 538')
    #os.system('adb shell input tap 996 136')  # 点击右上角关闭
def tmp():
    print('====== 进入领喵币中心，浏览杂项 ======')
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 1204 2278')  # 点击下方领喵币
    time.sleep(3)
    i = 0
    do=1
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    img = Image.open('screen.png')
    print(img.getpixel((1289, 1992)))
    if img.getpixel((1289, 1992)) == (174, 151, 147, 255):
        do = 0
    while do:
        os.system('adb shell screencap -p /sdcard/screen.png')
        os.system('adb pull /sdcard/screen.png')
        img = Image.open('screen.png')
        print(img.getpixel((1289, 1992)))
        i = i + 1
        if img.getpixel((1289, 1992)) == (174, 151, 147, 255):
            do = 0
        print('第{}次去浏览杂项...'.format(i))
        time.sleep(3)
        os.system('adb shell input tap 1289 1992')  # 点击去会场
        print('浏览杂项中，请等待15s...')
        time.sleep(17)
        os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
    print('已完成浏览杂项领取喵币任务')
screencap()
if f1 :
    qu_guang_dian()
if f2 :
    liu_lan_hui_chang()
if f3 :
    tmp()

