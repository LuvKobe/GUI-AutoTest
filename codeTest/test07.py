from pywinauto.application import Application

# # 打开Typora
# app = Application(backend='uia').connect(process=8016)
# win = app.window(title_re='.*po.*')
# win.wait("visible") # 保证窗口是可见的
#
# # 获取窗口的标题
# print(win.texts())


# # 打开Typora
# app = Application(backend='uia').connect(process=8016)
# win = app.window(title_re='.*po.*')
# win.wait("visible") # 保证窗口是可见的
#
# file = win.child_window(title="文件(​F)", control_type="MenuItem")
# print(file.texts())


# # 打开Typora
# app = Application(backend='uia').connect(process=8016)
# win = app.window(title_re='.*po.*')
# win.wait("visible") # 保证窗口是可见的
#
# print(win.window_text())

# 打开Typora
app = Application(backend='uia').connect(process=8016)
win = app.window(title_re='.*po.*')
win.wait("visible") # 保证窗口是可见的

file = win.child_window(title="文件(​F)", control_type="MenuItem")
print(file.window_text())