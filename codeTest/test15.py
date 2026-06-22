import datetime
import time

from pywinauto.application import Application

# 连接微信应用程序
app = Application(backend="uia").connect(process=15236)
win = app.window(title="Andy")
win.wait("visible") # 这里是为了让程序卡住等一下，直到计算器窗口完全显示在屏幕上，防止后面的操作因为窗口没加载完而报错。

# 0. 获取发送消息之前的消息个数
message_list = win.child_window(auto_id="chat_message_list", control_type="List")
message_count_before = message_list.item_count()

# 1. 更加精准地定位到微信聊天输入框
edit = app['Andy'].child_window(auto_id="chat_input_field", control_type="Edit")

# 2. 等待并唤起输入框
edit.wait("ready")

# 3. 点击输入框使其获取焦点
edit.click_input()

# 4. 输入文本（建议使用 type_keys）
message = "edison" + str(datetime.now())
edit.type_keys(message)
time.sleep(2)

# 5. 点击发送
send_btn = app['Andy'].child_window(title="发送", control_type="Button")
send_btn.click_input()

# 6. 获取发送消息之的消息个数
message_list = win.child_window(auto_id="chat_message_list", control_type="List")
message_count_after = message_list.item_count()
# 6.1 校验消息列表数量增加(1条 or 2条)
assert message_count_after == message_count_before + 1 or message_count_after == message_count_before + 2

# 6.2 获取列表里所有子控件的文本内容（会返回一个列表）
all_messages = message_list.texts()

# 6.3 打印出来肉眼看一下结构（调试用）
print("当前聊天记录里的文本：", all_messages)