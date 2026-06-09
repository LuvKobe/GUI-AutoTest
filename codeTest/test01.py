import time
from pywinauto.application import Application

# 1. 启动应用程序
Application(backend="uia").start("notepad.exe")
time.sleep(2)  # 等待 2 秒让记事本完全打开

# 2. 精确连接到刚刚打开的“无标题 - 记事本”
app = Application(backend="uia").connect(title="无标题 - 记事本")

# 3. 获取窗口对象（直接获取该进程的顶层窗口，防止标题对不上）
notepad = app.top_window()

# 4. 操作控件：在 Win10 的 Edit 控件中输入文本
notepad.Edit.type_keys("Hello, Pywinauto!", with_spaces=True)
print("输入成功!\n")

# 5. 关闭应用程序
time.sleep(1) # 稍微停顿一下让你看清文字输入进去了
notepad.close()