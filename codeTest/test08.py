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


 