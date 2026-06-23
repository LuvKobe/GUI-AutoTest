import math
import time

import pytest
from pywinauto import mouse

from utils.logUtils import Logger
from utils.yamlUtils import read_yaml

@pytest.mark.order(3)
class TestLocal:
    '''
    测试本地下载模块——文本
    “本地音乐、歌曲名称、歌手名称、专辑名称”
    '''
    def test_local_text(self,QQMusic_app):
        local_ele = read_yaml("本地下载")
        #点击导航栏-本地下载，进入本地下载页面
        local = QQMusic_app.win.child_window(auto_id=local_ele["auto_id"],
                                             control_type=local_ele["control_type"])
        local.click_input()
        #测试“本地音乐文本"
        local_text_ele = local_ele["本地音乐文本"]
        local_text = QQMusic_app.win.child_window(auto_id=local_text_ele["auto_id"],
                                             control_type=local_text_ele["control_type"]).window_text()
        assert local_text == "本地音乐"

        #测试“歌曲名称文本"
        songname_text_ele = local_ele["歌曲名称文本"]
        songname_text = QQMusic_app.win.child_window(auto_id=songname_text_ele["auto_id"],
                                             control_type=songname_text_ele["control_type"]).window_text()
        assert songname_text == "歌曲名称"

        #测试“歌手名称文本"
        singername_text_ele = local_ele["歌手名称文本"]
        singername_text = QQMusic_app.win.child_window(auto_id=singername_text_ele["auto_id"],
                                                     control_type=singername_text_ele["control_type"]).window_text()
        assert singername_text == "歌手名称"

        #测试“专辑名称文本"
        Albumname_text_ele = local_ele["专辑名称文本"]
        Albumrname_text = QQMusic_app.win.child_window(auto_id=Albumname_text_ele["auto_id"],
                                                       control_type=Albumname_text_ele["control_type"]).window_text()
        assert Albumrname_text == "专辑名称"

    '''
    测试本地下载模块——播放全部功能
    '''
    def test_local_playAll(self,QQMusic_app):
        local_ele = read_yaml("本地下载")
        playAll_ele = local_ele["播放全部"]
        playAll_btn = QQMusic_app.win.child_window(auto_id=playAll_ele["auto_id"],
                                                       control_type=playAll_ele["control_type"])
        #点击播放全部按钮
        playAll_btn.click_input()
        #获取播放进度
        process_line_ele = read_yaml("播放控制")["当前播放进度"]
        process_line_before = QQMusic_app.win.child_window(auto_id=process_line_ele["auto_id"],
                                                       control_type=process_line_ele["control_type"])
        process_line_len_before = process_line_before.rectangle().right
        #等待两秒
        time.sleep(2)
        #获取播放进度
        process_line_after = QQMusic_app.win.child_window(auto_id=process_line_ele["auto_id"],
                                                    control_type=process_line_ele["control_type"])
        process_line_len_after = process_line_after.rectangle().right
        #测试前后两个进度是否存在差别
        assert process_line_len_before != process_line_len_after

    '''
    测试本地下载模块——选择歌曲并双击播放
    '''
    def test_local_playSingle(self,QQMusic_app):
        music_list_ele = read_yaml("歌曲列表")
        music_list = QQMusic_app.win.child_window(auto_id=music_list_ele["auto_id"],
                                                    control_type=music_list_ele["control_type"])
        #将歌曲列表还原到最上方——————公共模块测试循环播放找最后一首歌曲将列表拉到了最下面
        point = music_list.rectangle().mid_point()
        mouse.scroll(coords=(point.x,point.y),wheel_dist=500)
        #获取歌曲列表中歌曲数量
        if music_list.item_count() <= 0:
            assert 0,"歌曲列表为空"
        #选择一首歌曲并双击播放
        point = music_list.get_item(row=0).rectangle().mid_point()
        mouse.double_click(coords=(point.x,point.y))
        # 获取播放进度
        process_line_ele = read_yaml("播放控制")["当前播放进度"]
        process_line_before = QQMusic_app.win.child_window(auto_id=process_line_ele["auto_id"],
                                                           control_type=process_line_ele["control_type"])
        process_line_len_before = process_line_before.rectangle().right
        # 等待两秒
        time.sleep(2)
        # 获取播放进度
        process_line_after = QQMusic_app.win.child_window(auto_id=process_line_ele["auto_id"],
                                                          control_type=process_line_ele["control_type"])
        process_line_len_after = process_line_after.rectangle().right
        # 测试前后两个进度是否存在差别
        assert process_line_len_before != process_line_len_after

    '''
    将歌曲标记喜欢——为了后面我喜欢模块的测试提供数据
    '''
    def test_mark_like(self,QQMusic_app):
        #获取歌曲列表中歌曲数量
        music_list_ele = read_yaml("歌曲列表")
        music_list = QQMusic_app.win.child_window(auto_id=music_list_ele["auto_id"],
                                                  control_type=music_list_ele["control_type"])
        list_size = music_list.item_count()
        #对每一首歌曲标记喜欢
        for i in range(0,list_size):
            if i != 0 and i % 6 == 0:
                #6及以后的歌曲在标记喜欢之前需要先向下滑动，使其显示出来
                point = music_list.rectangle().mid_point()
                mouse.scroll(coords=(point.x,point.y),wheel_dist=-500)
            rec = music_list.get_item(row=i).rectangle()
            #获取爱心的中间位置(x,y)
            y = math.floor((rec.top + rec.bottom)/2)
            x = rec.left + 22
            mouse.click(coords=(x,y))