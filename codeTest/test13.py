from pywinauto.application import Application
import time
import os

# 连接记事本窗口
#app = Application(backend="uia").connect(process=14940)
app = Application(backend='uia').start("C:\\Windows\\system32\\notepad.exe")
win = app.window(title_re='.*记事本.*')
win.wait("visible") # 保证窗口是可见的

# 批量创建五个文件
for i in range(1, 6):
    # 输入内容
    win.type_keys(f"创建第{i}个文件文件")

    # 等待保存文件窗口
    # 1)快捷键
    # win.type_keys(f"创建第{i}个文件文件^s")
    # 2)通过选择菜单选项
    #menu_bar = win.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
    #menu_bar.item_by_path(path="文件 -> 另存为").click_input()
    # 3)menu_select
    win.menu_select(path="文件 -> 另存为")

    # 切换到保存窗口
    save_win = win.child_window(title="另存为", control_type="Window")

    # 在保存弹窗上输入文件名称
    filename = f"D:\\GitHub_repository\\test_{i}.txt"
    save_win.child_window(title="文件名:", control_type="Edit").type_keys(filename)

    # 在保存弹窗上点击保存按钮
    save_win.child_window(title="保存(S)", control_type="Button").click_input()

    # 验证文件是否成功保存
    time.sleep(1)
    assert os.path.exists(filename)

    # 创建新文件
    win.type_keys("^n")