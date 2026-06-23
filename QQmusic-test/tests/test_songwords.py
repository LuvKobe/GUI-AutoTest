import math
import time

import pytest
from pywinauto import mouse

from utils.logUtils import Logger
from utils.yamlUtils import read_yaml

@pytest.mark.order(5)
class TestSongWords:
    logger = Logger.getlog()
    '''
    测试歌词页面的标题
    “歌手名、歌曲名”
    '''
    def test_titie_text(self,QQMusic_app):
        song_word_page_ele = read_yaml("歌词入口")
        song_word_btn = QQMusic_app.win.child_window(auto_id=song_word_page_ele["auto_id"],
                                     control_type=song_word_page_ele["control_type"])

        #点击页面的歌词入口，进入到歌词页面
        song_word_btn.click_input()
        #获取歌手名文本
        singer_text_ele = song_word_page_ele["歌手标题文本"]
        singer_text = QQMusic_app.win.child_window(auto_id=singer_text_ele["auto_id"],
                                     control_type=singer_text_ele["control_type"]).window_text()
        #校验歌手名文本
        assert singer_text == "刀郎"
        #获取歌曲名文本
        song_text_ele = song_word_page_ele["歌曲名标题文本"]
        song_text = QQMusic_app.win.child_window(auto_id=song_text_ele["auto_id"],
                                                   control_type=song_text_ele["control_type"]).window_text()
        #校验歌曲名文本
        assert song_text == "2002年的第一场雪"


    '''
    歌词页面——测试歌词
    从头播放歌曲并立即暂停————才能获取到歌词列表中的歌手名和歌曲名
    '''
    def test_songwords(self,QQMusic_app):
        likepage_ele = read_yaml("我喜欢")
        wordspage_ele = read_yaml("歌词入口")
        #收起歌词页面
        hide_word_page_ele = wordspage_ele["收起歌词"]
        hide_word_page_btn = QQMusic_app.win.child_window(auto_id=hide_word_page_ele["auto_id"],
                                     control_type=hide_word_page_ele["control_type"])
        hide_word_page_btn.click_input()

        # 为后面的测试用例做准备————点击播放歌曲并立即暂停
        playAll_ele = likepage_ele["播放全部"]
        playAll_btn = QQMusic_app.win.child_window(auto_id=playAll_ele["auto_id"],
                                                   control_type=playAll_ele["control_type"])
        playAll_btn.click_input()
        # 立即暂停播放
        play_ele = read_yaml("播放控制")["播放"]
        play_btn = QQMusic_app.win.child_window(auto_id=play_ele["auto_id"],
                                                control_type=play_ele["control_type"])
        play_btn.click_input()

        # 获取当前正在播放的歌手名和歌曲名
        play_control_ele = read_yaml("播放控制")
        singer_name_ele = play_control_ele["歌手名"]
        song_name_ele = play_control_ele["歌曲名"]
        singer_name = QQMusic_app.win.child_window(auto_id=singer_name_ele["auto_id"],
                                     control_type=singer_name_ele["control_type"]).window_text()
        song_name = QQMusic_app.win.child_window(auto_id=song_name_ele["auto_id"],
                                     control_type=song_name_ele["control_type"]).window_text()

        # songwordsText = f"{song_name} - {singer_name}"

        #进入歌词页面
        song_word_page_ele = read_yaml("歌词入口")
        song_word_btn = QQMusic_app.win.child_window(auto_id=song_word_page_ele["auto_id"],
                                                     control_type=song_word_page_ele["control_type"])

        # 点击页面的歌词入口，进入到歌词页面
        song_word_btn.click_input()
        #测试歌词
        words_list_ele = wordspage_ele["歌词列表"]
        words_list = QQMusic_app.win.child_window(auto_id=words_list_ele["auto_id"],
                                                     control_type=words_list_ele["control_type"])
        for i in words_list.children():
            if i.window_text() in song_name or i.window_text() in singer_name:
                return
            self.logger.info(f"获取到的歌词:{i.window_text()}")
        #始终没有匹配上
        raise Exception(f"歌词匹配失败，song_name:{song_name},singer_name{singer_name}")