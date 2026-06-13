from pywinauto.application import Application

# app = Application(backend='uia').connect(process=5092)
# win = app.window(best_match="Untitled• - Typora")
#
# print(win.print_control_identifiers())

# # 创建Application对象，连接到正在运行的Typora进程
# app = Application(backend='uia').connect(process=5092)
#
# # 获取与Typora相关的窗口对象，使用正则表达式匹配窗口标题
# win = app.window(best_match="Untitled• - Typora")
#
# # 等待窗口变为可见状态，确保窗口已经加载完成
# win.wait("visible")
#
# # 通过窗口的标题获取菜单对象
# menu = win['Menu2']
#
# # 打印菜单项的列表，查看菜单中包含的所有选项
# print(menu.items())


# 创建Application对象，连接到正在运行的Typora进程
app = Application(backend='uia').connect(process=5092)

# 获取与Typora相关的窗口对象，使用正则表达式匹配窗口标题
win = app.window(best_match="Untitled• - Typora")

# 等待窗口变为可见状态，确保窗口已经加载完成
win.wait("visible")

# 存在相同的auto_id和control_type，使用found_index来定位
menu = win.child_window(auto_id="", control_type="MenuItem", found_index=2)

# 打印菜单项的列表，查看菜单中包含的所有选项
print(menu.texts())