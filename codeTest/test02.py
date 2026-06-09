import time
from pywinauto.application import Application

# 启动应用程序
#Application(backend="uia").start("C:\\Windows\\system32\\notepad.exe")

# 通过connect连接已经打开的应用程序
#Application(backend="uia").connect(process=11556)

# # 打开应用程序
# app = Application(backend="uia").start("C:\\Windows\\system32\\notepad.exe")
#
# # 连接已经打开的应用程序
# # 通过pid连接
# # 获取应用程序对应的pid
# # app = Application(backend="uia").connect(process=app.process)
# app = Application(backend="uia").connect(process=1704)
#
# # 通过句柄连接
# app = Application(backend="uia").connect(handle=65552)


#app = Application(backend="uia").start("E:\\Typora195\\Typora\\Typora.exe")
# 通过connect连接已经打开的应用程序
# app = Application(backend="uia").connect(process=20184)
#
# # title--精确匹配
# win = app.window(title="Untitled• - Typora")
#
# # title_re--正则匹配
# win = app.window(title_re=".*po.*")
#
# # class_name--精确匹配
# win = app.window(class_name="Chrome_WidgetWin_1")
#
# # class_name--正则匹配
# win = app.window(class_name_re=".*Win_1")
#
# # best_match--模糊匹配
# win = app.window(best_match="Untitled")
#
# win.wait("visible")
# win.print_control_identifiers()


# 通过动态解析对象属性定位
'''
Pane - 'Untitled• - Typora'    (L1212, T71, R1903, B1011)
['Untitled• - Typora', 'Pane', 'Untitled• - TyporaPane', 'Pane0', 'Pane1']
child_window(title="Untitled• - Typora", control_type="Pane")
'''
# app = Application(backend="uia").connect(process=20184)
#
# #win = app.Pane
# #win = app['Untitled• - Typora']
#
# win = app.window(best_match="Untitled• - Typora")
#
# win.wait("visible")


app = Application(backend="uia").connect(process=20184)
win = app.top_window()
win.wait('exists')
print(win.print_control_identifiers())