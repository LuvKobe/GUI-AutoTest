import math
import time

import pytest
from pywinauto import mouse

from utils.logUtils import Logger
from utils.yamlUtils import read_yaml

@pytest.mark.order(4)
class TestLike:
    '''
    测试我喜欢——文本
    “我喜欢、歌曲名称、歌手名称、专辑名称”
    '''
    def test_like_text(self,QQMusic_app):
        like_ele = read_yaml("我喜欢")
        #点击导航栏“我喜欢”进入到我喜欢模块
        like_btn = QQMusic_app.win.child_window(auto_id=like_ele["auto_id"],
                                     control_type=like_ele["control_type"])
        like_btn.click_input()
        #测试“我喜欢”文本
        like_text_ele = like_ele["我喜欢文本"]
        like_text = QQMusic_app.win.child_window(auto_id=like_text_ele["auto_id"],
                                     control_type=like_text_ele["control_type"]).window_text()
        assert like_text == "我喜欢"

        #测试“歌曲名称”文本
        songname_text_ele = like_ele["歌曲名称文本"]
        songname_text = QQMusic_app.win.child_window(auto_id=songname_text_ele["auto_id"],
                                     control_type=songname_text_ele["control_type"]).window_text()
        assert songname_text == "歌曲名称"

        #测试“歌手名称”文本
        singername_text_ele = like_ele["歌手名称文本"]
        singername_text = QQMusic_app.win.child_window(auto_id=singername_text_ele["auto_id"],
                                                     control_type=singername_text_ele["control_type"]).window_text()
        assert singername_text == "歌手名称"

        #测试“专辑名称”文本
        albumrname_text_ele = like_ele["专辑名称文本"]
        albumrname_text = QQMusic_app.win.child_window(auto_id=albumrname_text_ele["auto_id"],
                                                       control_type=albumrname_text_ele["control_type"]).window_text()
        assert albumrname_text == "专辑名称"

    '''
    我喜欢模块——播放全部
    '''
    def test_like_playAll(self,QQMusic_app):
        playAll_ele = read_yaml("我喜欢")["播放全部"]
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
        #比较前后两次进度变化，有变化则说明按钮没有问题
        assert process_line_len_before != process_line_len_after

    '''
    我喜欢模块——选择歌曲双击播放
    '''
    def test_like_playSingle(self,QQMusic_app):
        music_list_ele = read_yaml("我喜欢")["歌曲列表"]
        music_list = QQMusic_app.win.child_window(auto_id=music_list_ele["auto_id"],
                                     control_type=music_list_ele["control_type"])
        #获取歌曲列表歌曲数量
        list_size = music_list.item_count()
        if list_size <= 0:
            assert 0,"歌曲列表为空"
        #选择第一首歌曲双击播放
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
        # 比较前后两次进度变化，有变化则说明双击歌曲播放没有问题
        assert process_line_len_before != process_line_len_after

    '''
    我喜欢模块——测试标记喜欢
    '''
    def test_mark_unLike(self,QQMusic_app):
        #获取歌曲列表中歌曲的数量
        music_list_ele = read_yaml("我喜欢")["歌曲列表"]
        music_list_before = QQMusic_app.win.child_window(auto_id=music_list_ele["auto_id"],
                                                  control_type=music_list_ele["control_type"])
        # 获取歌曲列表歌曲数量
        list_size_before = music_list_before.item_count()
        #取消标记喜欢
        rec = music_list_before.get_item(row=0).rectangle()
        y = math.floor((rec.top + rec.bottom)/2)
        x = rec.left + 22
        mouse.click(coords=(x,y))
        #获取歌曲列表中歌曲的数量
        music_list_after = QQMusic_app.win.child_window(auto_id=music_list_ele["auto_id"],
                                                         control_type=music_list_ele["control_type"])
        # 获取歌曲列表歌曲数量
        list_size_after = music_list_after.item_count()
        #测试取消标记喜欢是否成功
        assert list_size_after + 1 == list_size_before