from pywinauto.application import Application

app = Application(backend='uia').connect(process=20184)
win = app.window(title_re='.*po.*')
# 添加等待
win.wait('exists')

# 最小化
win.minimize()
print("is_minimized:", win.is_minimized())

win.maximize()
print("is_maximized:", win.is_maximized())

win.restore()
print("is_normal", win.is_normal())

print("get_show_state:", win.get_show_state())
print("is_dialog", win.is_dialog())

win.close()