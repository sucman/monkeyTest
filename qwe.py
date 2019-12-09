import os

def getPackage():
    getdevices = os.popen("ls")  # adb shell dumpsys window | findstr mCurrentFocus
    text = getdevices.read()
    print(text)
    return text

a = getPackage()
print(a)