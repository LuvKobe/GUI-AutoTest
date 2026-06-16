import time

from pywinauto import mouse
from pywinauto.application import Application

#连接抖音
app = Application(backend="uia").connect(process=13864)
#定位窗口
win = app.window(title="抖音")
win.wait("visible")

for i in range(0,3):
    #双击视频刷赞
    point = win.rectangle().mid_point()

    time.sleep(2) # 休眠
    #调用高级api双击
    win.double_click_input()
    # #鼠标操作
    # mouse.double_click(coords=(point.x,point.y))
    #刷到下一个视频
    time.sleep(2)
    mouse.scroll(coords=(point.x,point.y),wheel_dist=-500)