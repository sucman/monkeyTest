# -*- coding:utf-8 -*-
"""
"""
import os
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("monkeyTest")
win.geometry("500x500+100+100")
win.resizable(False, False)


def getDevices():
    getpackage = os.popen("adb devices")
    text = getpackage.read()
    return text


def getPackage():
    getdevices = os.popen("ifconfig")  # adb shell dumpsys window | findstr mCurrentFocus
    text = getdevices.read()
    return text


def clic1():
    devicesVar.set(getDevices())


def clic2():
    packageVar.set(getPackage())


def getThrottle():
    throttle = throttleEntry.get()
    return throttle


def getCount():
    count = countEntry.get()
    return count


def getSeed():
    seed = seedEntry.get()
    return seed


# ComboBox
logVar = tk.StringVar()  # 绑定变量

logComboBox = ttk.Combobox(win, textvariable=logVar)
logComboBox.grid(row=3, column=1)
# 设置下拉数据
logComboBox["value"] = ("0", "1", "2")
# 设置默认值
logComboBox.current(0)


# 绑定事件
def func(event):
    print(logComboBox.get())
    print(logVar.get())


logComboBox.bind("<<ComboboxSelected>>", func)

# Lable
devicesLable = tk.Label(win, text="设备信息:")
devicesLable.grid(row=0, column=0, sticky="W")
packageLable = tk.Label(win, text="-p 包名")
packageLable.grid(row=1, column=0, sticky="W")
throttleLable = tk.Label(win, text="-throttle 延时（ms）")
throttleLable.grid(row=2, column=0, sticky="W")
logLable = tk.Label(win, text="-v 日志级别")
logLable.grid(row=3, column=0, sticky="W")
countLable = tk.Label(win, text="count 随机事件数")
countLable.grid(row=4, column=0, sticky="W")
seedLable = tk.Label(win, text="s 种子")
seedLable.grid(row=5, column=0, sticky="W")

# Entry
devicesVar = tk.StringVar()
devicesEntry = tk.Entry(win, textvariable=devicesVar)
devicesEntry.grid(row=0, column=1, sticky="W")
packageVar = tk.StringVar()
packageEntry = tk.Entry(win, textvariable=packageVar)
packageEntry.grid(row=1, column=1, sticky="W")
throttleEntry = tk.Entry(win)
throttleEntry.grid(row=2, column=1, sticky="W")
countEntry = tk.Entry(win)
countEntry.grid(row=4, column=1, sticky="W")
seedEntry = tk.Entry(win)
seedEntry.grid(row=5, column=1, sticky="W")

# Button
devicesButton = tk.Button(win, text="获取", command=clic1)
devicesButton.grid(row=0, column=3)
packageButton = tk.Button(win, text="获取", command=clic2)
packageButton.grid(row=1, column=3)
throttleButton = tk.Button(win, text="获取11", command=getThrottle)
throttleButton.grid(row=2, column=3)
countButton = tk.Button(win, text="获取22", command=getCount)
countButton.grid(row=4, column=3)
seedButton = tk.Button(win, text="获取33", command=getSeed)
seedButton.grid(row=5, column=3)

a = getPackage()

butMonkey = tk.Button(win, text="执行monkey测试",
                      command=lambda: os.popen("if%r", a)).grid(row=20, column=3)

# adb shell monkey -p %s --throttle %s -v -s %s %s >c:%s.txt
# subject = 'monkey测试报告 ' + str(time.strftime("%Y%m%d %H:%M:%S", time.localtime()))

win.mainloop()
