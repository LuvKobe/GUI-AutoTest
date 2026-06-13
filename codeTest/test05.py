from pywinauto.application import Application

# 创建Application对象，连接到正在运行的Typora进程
app = Application(backend='uia').connect(process=5092)

# 获取与Typora相关的窗口对象，使用正则表达式匹配窗口标题
win = app.window(title_re='.*po.*')

# 添加等待
win.wait('exists')

# 最小化
win.minimize()
print("is_minimized:", win.is_minimized())

win.maximize()
print("is_maximized:", win.is_maximized())

win.close()