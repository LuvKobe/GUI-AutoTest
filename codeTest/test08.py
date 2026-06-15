import time

from pywinauto import mouse
from pywinauto.application import Application

# # 打开Typora
# app = Application(backend='uia').connect(process=8016)
# win = app.window(title_re='.*po.*')
# win.wait("visible") # 保证窗口是可见的
#
# # 双击标题栏
# #title_bar = win['TitleBar']
# #title_bar.double_click_input(coords=(207,21))
#
# #通过鼠标点击
# mouse.double_click(coords=(207,21))

# 打开记事本
# app = Application(backend='uia').connect(process=5044)
# win = app.window(title_re='.*记事本.*')
# win.wait('visible')
#
# #定位滚动条
# right_ScrollBar = win.child_window(title="垂直滚动条", auto_id="NonClientVerticalScrollBar", control_type="ScrollBar")
# right_ScrollBar.wait('visible')
#
# #获取滚动条中间位置
# mid = right_ScrollBar.rectangle().mid_point()
# #从中间位置下拉
# mouse.scroll(coords=(mid.x, mid.y), wheel_dist=-900)

#mouse.scroll(coords=(900, 600), wheel_dist=-900)

# 连接计算器窗口
app = Application(backend="uia").connect(process=14752)
win = app.window(title="计算器")
win.wait("visible") # 这里是为了让程序卡住等一下，直到计算器窗口完全显示在屏幕上，防止后面的操作因为窗口没加载完而报错。

# 找到数字键盘区域
num_pad = win.child_window(title="数字键盘", auto_id="NumberPad", control_type="Group")

# 自动循环点击每一个数字
for num in num_pad.children(): # 遍历数字键盘里的每一个子按钮（比如数字 1、2、3...）。
    point = num.rectangle().mid_point() # 获取当前按钮在屏幕上的中心点坐标（X 轴和 Y 轴）。
    mouse.click(coords=(point.x, point.y)) # 控制你的真实鼠标指针，移动到这个中心点并执行点击。
    time.sleep(2)
