import math
import time

from pywinauto import mouse

from utils.logUtils import Logger
from utils.yamlUtils import read_yaml

class TestCommon:
    logger = Logger.getlog()
    '''
    测试logo
    '''
    def est_logo(self, QQMusic_app):
        logo_ele = read_yaml("logo")
        logo = QQMusic_app.win.child_window(auto_id=logo_ele['auto_id'], control_type=logo_ele["control_type"])
        #logo = QQMusic_app.win.child_window(auto_id="QQMusic.background.head.headLeft.logo", control_type="Text")
        logo.wait("visible")

    '''
    测试 - 搜索功能
    '''
    def est_search(self, QQMusic_app):
        edit_ele = read_yaml("search")
        edit = QQMusic_app.win.child_window(auto_id=edit_ele['auto_id'], control_type=edit_ele["control_type"])
        #edit = QQMusic_app.win.child_window(auto_id="QQMusic.background.head.headRight.searchBox.lineEdit", control_type="Edit")
        # 唤起输入框
        edit.click_input()
        # ctrl+a全部选中之后再输入关键词，就不会存在追加的情况
        edit.type_keys("^a周杰伦")

    '''
    测试——换皮肤
    '''
    def est_skin(self,QQMusic_app):
        skin_ele = read_yaml("换肤")
        skin = QQMusic_app.win.child_window(auto_id=skin_ele['auto_id'],
                                            control_type=skin_ele['control_type'])
        #点击换肤入口，唤起弹窗
        skin.click_input()

        #验证弹窗以及文本信息
        warning = QQMusic_app.win.child_window(title="温馨提示", control_type="Window")
        warning.wait("visible")

        warn_text = warning.child_window(control_type="Text").window_text()

        assert warn_text == "换肤功能小哥哥正在紧急支持中..."

        #关闭温馨提示弹窗
        warning.close()
        #测试弹窗是否正确关闭
        warning.wait_not("visible")

    '''
    测试——最小化
    '''
    def est_window_min(self,QQMusic_app):
        window_min_ele = read_yaml("最小化")
        window_min_btn = QQMusic_app.win.child_window(auto_id=window_min_ele['auto_id'],
                                                     control_type=window_min_ele['control_type'])
        #点击最小化按钮
        window_min_btn.click_input()

        #测试一下QQ音乐窗口是否已经最小化了
        assert QQMusic_app.win.is_minimized()
        #还原
        QQMusic_app.win.restore()

    '''
    测试——导入音乐
    '''
    def est_importMusic(self,QQMusic_app):
        import_ele = read_yaml("导入音乐")
        import_btn = QQMusic_app.win.child_window(auto_id=import_ele['auto_id'],
                                     control_type=import_ele['control_type'])
        #点击导入音乐按钮
        import_btn.click_input()

        #定位添加本地下载音乐窗口
        import_win = QQMusic_app.win.child_window(title="添加本地下载音乐",control_type="Window")
        import_win.wait("visible")

        #选中所有音乐并添加
        music_list = import_win.child_window(title="项目视图",control_type="List")
        #打开音乐：1）通过“打开”按钮来实现 2）enter键实现
        music_list.type_keys("^a{ENTER}")

        import_win.wait_not("visible")

    '''
    播放控制模块——随机播放
    默认模式就是随机播放
    默认是暂停
    '''
    def est_play_random(self,QQMusic_app):
        #点击播放全部
        local_ele = read_yaml("本地下载")
        play_all_ele = local_ele["播放全部"]
        play_btn = QQMusic_app.win.child_window(auto_id=play_all_ele['auto_id'],
                                     control_type=play_all_ele['control_type'])

        for i in range(1, 4):
            # 点击播放全部，从第一首歌曲开始播放（2002年的第一场雪）
            play_btn.click_input()
            # 将歌曲播放进度拉到尾部

            play_ele = read_yaml("播放控制")
            process_line_ele = play_ele["播放总进度"]
            process_line = QQMusic_app.win.child_window(auto_id=process_line_ele['auto_id'],
                                                        control_type=process_line_ele['control_type'])
            # 获取进度条的尺寸
            rec = process_line.rectangle()
            x = rec.right - 3
            y = math.floor((rec.top + rec.bottom) / 2)

            # 鼠标点击进度条的尾部
            mouse.click(coords=(x, y))

            # 等待切换下一曲
            time.sleep(2)
            # 检查下一步是否为列表中第二首歌曲
            #             1）若是，随机播放模式不一定错误
            #             2）若不是，随机播放模式正确
            music_name_ele = play_ele["歌曲名"]
            music_name = QQMusic_app.win.child_window(auto_id=music_name_ele['auto_id'],
                                                      control_type=music_name_ele['control_type']).window_text()
            if music_name != "Andy阿杜":
                self.logger.info(f"第{i}次判断随机播放下一曲正确")
                return
            else:
                self.logger.info(f"第{i}次判断随机播放下一曲错误")
            # 走到这里还没有返回
        raise Exception("随机播放下一曲三次判断均错误")

    '''
    播放控制模块——单曲循环
    默认模式就是随机播放--切换模式
    上一个用例执行完是播放
    '''
    def est_play_single(self,QQMusic_app):
        # 点击播放全部
        local_ele = read_yaml("本地下载")
        play_all_ele = local_ele["播放全部"]
        play_btn = QQMusic_app.win.child_window(auto_id=play_all_ele['auto_id'],
                                                control_type=play_all_ele['control_type'])
        #切换模式：随机播放——单曲循环
        play_ele = read_yaml("播放控制")
        playMode_ele = play_ele["模式切换"]
        playMode_btn = QQMusic_app.win.child_window(auto_id=playMode_ele['auto_id'],
                                                control_type=playMode_ele['control_type'])
        #点击切换模式按钮
        playMode_btn.click_input()

        for i in range(1,4):
            #点击播放全部按钮
            play_btn.click_input()

            music_name_ele = play_ele["歌曲名"]
            music_name_before = QQMusic_app.win.child_window(auto_id=music_name_ele['auto_id'],
                                                            control_type=music_name_ele['control_type']).window_text()


            # 将歌曲播放进度拉到尾部
            process_line_ele = play_ele["播放总进度"]
            process_line = QQMusic_app.win.child_window(auto_id=process_line_ele['auto_id'],
                                                        control_type=process_line_ele['control_type'])
            # 获取进度条的尺寸
            rec = process_line.rectangle()
            x = rec.right - 3
            y = math.floor((rec.top + rec.bottom) / 2)

            # 鼠标点击进度条的尾部
            mouse.click(coords=(x, y))

            # 等待切换下一曲
            time.sleep(2)
            #下一首播放的歌曲和前一首歌曲是否相同
            #        1）相同，单曲循环模式不一定正确---多次验证
            #        2）不相同，单曲循环模式错误
            music_name_after = QQMusic_app.win.child_window(auto_id=music_name_ele['auto_id'],
                                                      control_type=music_name_ele['control_type']).window_text()
            if music_name_before != music_name_after:
                self.logger.error(f"单曲循环模式播放下一首歌曲校验错误，before:{music_name_before},after:{music_name_after}")
                break
            else:
                self.logger.info(f"第{i}次校验单曲循环模式播放下一首歌曲正确")
                if i == 3:
                    return
        raise Exception(f"单曲循环模式播放下一首歌曲校验错误，before:{music_name_before},after:{music_name_after}")

    '''
    播放控制模块——列表循环
    默认模式就是单曲循环播放--切换模式
    上一个用例执行完是播放
    '''
    def test_play_circle(self,QQMusic_app):
        # 切换模式：单曲循环——列表循环
        play_ele = read_yaml("播放控制")
        music_name_ele = play_ele["歌曲名"]
        playMode_ele = play_ele["模式切换"]
        playMode_btn = QQMusic_app.win.child_window(auto_id=playMode_ele['auto_id'],
                                                    control_type=playMode_ele['control_type'])
        # 点击切换模式按钮
        playMode_btn.click_input()

        for i in range(1,4):
            #找到列表中最后一首歌曲
            music_list_ele = read_yaml("歌曲列表")
            music_list = QQMusic_app.win.child_window(auto_id=music_list_ele['auto_id'],
                                                    control_type=music_list_ele['control_type'])
            #获取歌曲列表的中间坐标
            list_mid = music_list.rectangle().mid_point()
            #鼠标下拉列表使其展示最后一首歌曲
            mouse.scroll(coords=(list_mid.x,list_mid.y),wheel_dist=-500)
            #获取最后一首歌曲——求列表中列表项目数
            list_size = music_list.item_count()
            #双击最后一首歌曲，使其播放
            last_music_mid = music_list.get_item(row=list_size-1).rectangle().mid_point()
            mouse.double_click(coords=(last_music_mid.x,last_music_mid.y))

            #拉取进度条到尾部，等待播放下一曲
            process_line_ele = play_ele["播放总进度"]
            process_line = QQMusic_app.win.child_window(auto_id=process_line_ele['auto_id'],
                                                        control_type=process_line_ele['control_type'])
            # 获取进度条的尺寸
            rec = process_line.rectangle()
            x = rec.right - 3
            y = math.floor((rec.top + rec.bottom) / 2)

            # 鼠标点击进度条的尾部
            mouse.click(coords=(x, y))

            # 等待切换下一曲
            time.sleep(2)
            # 校验播放的下一首歌曲是否为“2002年的第一场雪（列表的第一首歌曲）”
            #            1）是，列表循环校验不一定正确
            #            2）不是，列表循环校验错误
            music_name = QQMusic_app.win.child_window(auto_id=music_name_ele['auto_id'],
                                                            control_type=music_name_ele['control_type']).window_text()
            if music_name != "2002年的第一场雪":
                self.logger.error(f"列表循环下一曲错误,music_name:{music_name}")
                break
            else:
                self.logger.info(f"第{i}次校验列表循环下一曲正确")
                if i == 3:
                    return
        raise Exception(f"列表循环下一曲错误,music_name:{music_name}")