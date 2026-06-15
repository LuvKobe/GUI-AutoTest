import time

from pywinauto.application import Application

# # 打开计算器
# app = Application(backend="uia").connect(process=14752)
# win = app.window(title="计算器")
# win.wait("visible") # 保证窗口是可见的
# time.sleep(2)
#
# # 点击计算器上的按钮, 进行 1 + 2 = 3
#
# # 定位数字按钮1
# btn_1 = win.child_window(title="一", auto_id="num1Button", control_type="Button")
# # 点击数字按钮1
# btn_1.click_input()
# time.sleep(2)
#
# # 定位按钮+
# add_btn = win.child_window(title="加", auto_id="plusButton", control_type="Button")
# # 点击按钮+
# add_btn.click_input()
# time.sleep(2)
#
# # 定位数字按钮2
# btn_2 = win.child_window(title="二", auto_id="num2Button", control_type="Button")
# # 点击数字按钮2
# btn_2.click_input()
# time.sleep(2)
#
# # 定位按钮=
# equal_btn = win.child_window(title="等于", auto_id="equalButton", control_type="Button")
# # 点击按钮=
# equal_btn.click_input()
# time.sleep(5)


# # 打开Typora
# app = Application(backend='uia').connect(process=8016)
# win = app.window(title_re='.*po.*')
# win.wait("visible") # 保证窗口是可见的
# print(win.print_control_identifiers())
# # 对窗口进行右键操作
# win.right_click_input()


# 打开Typora
app = Application(backend='uia').connect(process=8016)
win = app.window(title_re='.*po.*')
win.wait("visible") # 保证窗口是可见的

# 双击标题栏
title_bar = win['TitleBar']
title_bar.double_click_input()