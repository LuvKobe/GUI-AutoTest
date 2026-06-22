from pywinauto.application import Application

# # 连接记事本窗口
# app = Application(backend="uia").connect(process=14940)
# win = app.window(title_re='.*记事本.*')
# win.wait("visible") # 保证窗口是可见的
#
# #win.print_control_identifiers()
#
# # 获取所有的菜单项
# menu_bar = win.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
# #print(menu_bar.items())
#
# print(menu_bar.item_by_index(0))
# print(menu_bar.item_by_index(1))
# print(menu_bar.item_by_index(2))
# print(menu_bar.item_by_index(3))
# print(menu_bar.item_by_index(4))


# 连接记事本窗口
app = Application(backend="uia").connect(process=14940)
win = app.window(title_re='.*记事本.*')
win.wait("visible") # 保证窗口是可见的

#win.print_control_identifiers()

# 获取所有的菜单项
menu_bar = win.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
#print(menu_bar.items())

# 选择保存文件
menu_bar.item_by_path(path="文件 -> 另存为").click_input()
