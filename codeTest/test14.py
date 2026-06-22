from pywinauto.application import Application

# # 连接记事本窗口
# app = Application(backend="uia").connect(process=7348)
# win = app.window(title_re='.*文件资源管理器')
# win.wait("visible") # 保证窗口是可见的
#
# # 定位列表控件
# list_ctrol = win.child_window(title="项目视图", control_type="List")

# 打印子控件信息
#print(list_ctrol.get_items())

# # 连接记事本窗口
# app = Application(backend="uia").connect(process=7348)
# win = app.window(title_re='.*文件资源管理器')
# win.wait("visible") # 保证窗口是可见的
#
# # 定位列表控件
# list_ctrol = win.child_window(title="项目视图", control_type="List")
#
# #打印列表项数量
# print("items:",list_ctrol.item_count())

# 连接记事本窗口
app = Application(backend="uia").connect(process=7348)
win = app.window(title_re='.*文件资源管理器')
win.wait("visible") # 保证窗口是可见的

# 定位列表控件
list_ctrol = win.child_window(title="项目视图", control_type="List")

#获取列表中第一项
print("items:",list_ctrol.get_item(row=0))