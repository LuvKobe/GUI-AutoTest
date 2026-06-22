import pytest
from pywinauto import Application
from utils.logUtils import Logger

class QQmusicApp:
    def __init__(self):
        self.app_path = r"D:\GitHub_repository\qqmusic\QQMusic.exe"
        self.logger = Logger.getlog()
        self.app = None
        self.win = None

    #启动QQmusic程序
    def launch(self):
        try:
            self.app = Application(backend="uia").start(self.app_path)
            #测试代码
            # self.app = Application(backend="uia").connect(process=4060)
            #定位窗口
            self.win = self.app.window(title="QQMusic")
            self.win.wait("visible")
            self.logger.info("应用程序启动成功！")
            # self.win.print_control_identifiers()

        except Exception as e:
            self.logger.error(f"应用程序启动失败:{e}")

    #关闭QQmusic程序
    def close(self):
        if self.win:
            self.win.close()

@pytest.fixture(scope="session")
def QQMusic_app():
    QQmusic = QQmusicApp()
    QQmusic.launch()

    yield QQmusic

    QQmusic.close()