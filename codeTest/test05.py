from pywinauto.application import Application
from pywinauto.timings import wait_until

# # 创建Application对象，连接到正在运行的Typora进程
# app = Application(backend='uia').connect(process=5092)
#
# # 获取与Typora相关的窗口对象，使用正则表达式匹配窗口标题
# win = app.window(title_re='.*po.*')
#
# # 添加等待
# win.wait('exists')
#
# # 最小化
# win.minimize()
# print("is_minimized:", win.is_minimized())
#
# win.maximize()
# print("is_maximized:", win.is_maximized())
#
# win.close()

# # 创建Application对象，连接到正在运行的Typora进程
# app = Application(backend='uia').connect(process=5092)
#
# # 获取与Typora相关的窗口对象，使用正则表达式匹配窗口标题
# win = app.window(title_re='.*po.*')
#
# # 检查窗口是有效的句柄
# win.wait('exists')
#
# # 检查窗口是否可见
# win.wait('visible')
#
# # 检查窗口是否未被禁用
# win.wait('enabled')
#
# # 检查窗口是否准备就绪
# win.wait('ready')

# # 打开计算器
# # app = Application(backend="uia").start("calc.exe")
# app = Application(backend="uia").connect(process=14752)
# win = app.window(title="计算器")
# win.wait("visible")
#
# # 启用的按钮
# enable_btn = win.child_window(title="记忆加法", auto_id="MemPlus", control_type="Button")
#
# # 未启用的按钮
# disabled_btn = win.child_window(title="清除所有记忆", auto_id="ClearMemoryButton", control_type="Button")
#
# enable_btn.wait("enabled")       # 代码执行通过
# disabled_btn.wait_not("enabled") # 代码执行通过
# #disabled_btn.wait("enabled") # 代码执行不通过 -- 会超时

# 打开计算器
# app = Application(backend="uia").start("calc.exe")
# app = Application(backend="uia").connect(process=14752)
# win = app.window(title="计算器")
# win.wait("visible")
#
# # 启用的按钮
# enable_btn = win.child_window(title="记忆加法", auto_id="MemPlus", control_type="Button")
#
# # 未启用的按钮
# disabled_btn = win.child_window(title="清除所有记忆", auto_id="ClearMemoryButton", control_type="Button")
#
# enable_btn.wait("enabled")       # 代码执行通过
# disabled_btn.wait_not("enabled") # 代码执行通过
# #disabled_btn.wait("enabled") # 代码执行不通过 -- 会超时

# # 打开计算器
# app = Application(backend="uia").connect(process=14752)
# win = app.window(title="计算器")
# win.wait("exists")
#
# proc = win.child_window(title="打开导航", auto_id="TogglePaneButton", control_type="Button")
# proc.wait("ready") # 等待成功
#
# proc_chid = win.child_window(auto_id="PaneTitleTextBlock", control_type="Text")
# proc_chid.wait("ready") # 等待失败

# # 打开计算器
# app = Application(backend="uia").connect(process=14752)
# win = app.window(title="计算器")
#
# # 把焦点放到计算器上
# win.set_focus()
#
# # 先对计算器进行操作: 输入1
# num1_btn = win.child_window(title="一", auto_id="num1Button", control_type="Button")
#
# # 点击按钮
# num1_btn.click_input()
#
# # 等待成功
# win.wait("active")

# i = 0
# def work():
#     global i
#     i += 1
#     print("当前i的值为", i)
#     return i
#
# # 等待work返回的结果为5，继续往下执行
# wait_until(10, 1, work, 5)
# print("等待通过")


def get_window():
    app = Application(backend="uia").connect(process=14752)
    win = app.window(title="计算器")
    return win.is_visible() # 验证窗口是否为可见状态(必须打开窗口)

def test_wait():
    # 5s钟内等待get_window方法返回结果为True
    wait_until(5, 2, get_window, True)
    print("等待通过")

test_wait()