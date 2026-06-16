import time

from pywinauto import mouse
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

#send_keys("1234567")

# # 连接记事本窗口
# app = Application(backend="uia").connect(process=4884)
# win = app.window(title_re='.*记事本.*')
# win.wait("visible") # 保证窗口是可见的
#
# # 在记事本中输入内容
# #输入文本内容
# win.type_keys("---type_keys---")
#
# #保留换行符
# win.type_keys("---type_keys---\n",with_newlines=True)
#
# #保留空格
# win.type_keys(" ----type keys---- ",with_spaces=True)
#
# #延迟输入，避免输入过快导致内容不完整
# win.type_keys("一二三四五六七",with_spaces=True)

# # 连接记事本窗口
# app = Application(backend="uia").connect(process=4884)
# win = app.window(title_re='.*记事本.*')
# win.wait("visible") # 保证窗口是可见的
#
# # 在记事本中输入内容
# #发送文本和回车
# win.type_keys("Hello World{ENTER}",with_spaces=True)
# win.type_keys("Hello edison",with_spaces=True)

# # 连接记事本窗口
# app = Application(backend="uia").connect(process=4884)
# win = app.window(title_re='.*记事本.*')
# win.wait("visible") # 保证窗口是可见的
#
# # 在记事本中输入内容
# #发送文本和回车
# win.type_keys("Hello World{ENTER 2}",with_spaces=True)
# win.type_keys("Hello edison",with_spaces=True)

# 连接记事本窗口
app = Application(backend="uia").connect(process=4884)
win = app.window(title_re='.*记事本.*')
win.wait("visible") # 保证窗口是可见的

# 在记事本中输入内容
win.type_keys("1+2=3{ENTER}")  # 错误：'+' 会被识别为 Shift
win.type_keys("2{+}3=5")       # 正确