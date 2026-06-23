import pytest
from pywinauto import mouse

from utils.logUtils import Logger
from utils.yamlUtils import read_yaml

class TestRecommend:
    logger = Logger.getlog()
    '''
    测试——推荐页面的文本
    "推荐、今日为你推荐、你的音乐补给"
    '''
    def test_rec_text(self,QQMusic_app):
        #点击左侧的推荐导航入口，进入到推荐页面
        rec_ele = read_yaml("推荐")
        rec_btn = QQMusic_app.win.child_window(auto_id=rec_ele["auto_id"],
                                           control_type=rec_ele["control_type"])
        rec_btn.click_input()
        #获取“推荐”文本控件
        rec_text_ele = rec_ele["推荐文本"]
        #获取“今日为你推荐”文本控件
        rec_foru_text_ele = rec_ele["今日为你推荐文本"]
        #获取“你的音乐补给”文本控件
        rec_supply_text_ele = rec_ele["你的音乐补给文本"]

        #校验“推荐”文本控件
        rec_text =  QQMusic_app.win.child_window(auto_id=rec_text_ele["auto_id"],
                                           control_type=rec_text_ele["control_type"])
        assert rec_text.window_text() == "推荐"

        # 校验“今日为你推荐”文本控件
        rec_foru_text = QQMusic_app.win.child_window(auto_id=rec_foru_text_ele["auto_id"],
                                           control_type=rec_foru_text_ele["control_type"])
        assert rec_foru_text.window_text() == "今日为你推荐"

        #校验“你的音乐补给”文本控件
        rec_supply_text = QQMusic_app.win.child_window(auto_id=rec_supply_text_ele["auto_id"],
                                           control_type=rec_supply_text_ele["control_type"])
        assert rec_supply_text.window_text() == "你的音乐补给"

    '''
    测试今日为你推荐滚动区域——左滚动
    '''
    def test_recforu_scroll_left(self,QQMusic_app):
        rec_ele = read_yaml("推荐")

        item_text_ele = rec_ele["今日为你推荐第一项文本"]
        item_text_before = QQMusic_app.win.child_window(auto_id=item_text_ele["auto_id"],
                                           control_type=item_text_ele["control_type"],
                                            found_index=0).window_text()

        scroll_left_ele = rec_ele["今日为你推荐左滚动"]
        scroll_left = QQMusic_app.win.child_window(auto_id=scroll_left_ele["auto_id"],
                                           control_type=scroll_left_ele["control_type"])
        #点击左滚动按钮
        scroll_left.click_input()
        #获取推荐项的名称，进行前后对比校验
        item_text_after = QQMusic_app.win.child_window(auto_id=item_text_ele["auto_id"],
                                           control_type=item_text_ele["control_type"],
                                            found_index=0).window_text()

        assert item_text_before != item_text_after

    '''
    测试今日为你推荐滚动区域——右滚动
    '''
    def test_recforu_scroll_right(self, QQMusic_app):
        rec_ele = read_yaml("推荐")

        item_text_ele = rec_ele["今日为你推荐第一项文本"]
        item_text_before = QQMusic_app.win.child_window(auto_id=item_text_ele["auto_id"],
                                                        control_type=item_text_ele["control_type"],
                                                        found_index=0).window_text()

        scroll_right_ele = rec_ele["今日为你推荐右滚动"]
        scroll_right = QQMusic_app.win.child_window(auto_id=scroll_right_ele["auto_id"],
                                                   control_type=scroll_right_ele["control_type"])
        # 点击右滚动按钮
        scroll_right.click_input()
        # 获取推荐项的名称，进行前后对比校验
        item_text_after = QQMusic_app.win.child_window(auto_id=item_text_ele["auto_id"],
                                                       control_type=item_text_ele["control_type"],
                                                       found_index=0).window_text()

        assert item_text_before != item_text_after

    '''
    测试——你的音乐补给滚动区域——左滚动
    '''
    def test_supply_scroll_left(self,QQMusic_app):
        rec_ele = read_yaml("推荐")
        all_rec_area_ele = rec_ele["推荐整个模块"]
        all_rec_area = QQMusic_app.win.child_window(auto_id=all_rec_area_ele["auto_id"],
                                     control_type=all_rec_area_ele["control_type"])
        #找推荐整个模块的中间坐标
        point = all_rec_area.rectangle().mid_point()
        #在推荐模块鼠标下拉，展示完整的为你推荐区域
        mouse.scroll(coords=(point.x,point.y),wheel_dist=-500)
        #点击左滚动按钮
        scroll_left_ele = rec_ele["音乐补给左滚动"]
        one_one_ele = rec_ele["音乐补给第一排第一项文本"]
        two_one_ele = rec_ele["音乐补给第二排第一项文本"]

        one_one_text_before = QQMusic_app.win.child_window(auto_id=one_one_ele["auto_id"],
                                                       control_type=one_one_ele["control_type"],
                                                    found_index=0).window_text()
        two_one_text_before = QQMusic_app.win.child_window(auto_id=two_one_ele["auto_id"],
                                                       control_type=two_one_ele["control_type"],
                                                    found_index=0).window_text()

        scroll_left_btn = QQMusic_app.win.child_window(auto_id=scroll_left_ele["auto_id"],
                                     control_type=scroll_left_ele["control_type"])
        scroll_left_btn.click_input()
        #左滚动结果的校验--项目名称是否变化
        one_one_text_after = QQMusic_app.win.child_window(auto_id=one_one_ele["auto_id"],
                                                           control_type=one_one_ele["control_type"],
                                                           found_index=0).window_text()
        two_one_text_after = QQMusic_app.win.child_window(auto_id=two_one_ele["auto_id"],
                                                           control_type=two_one_ele["control_type"],
                                                           found_index=0).window_text()
        assert one_one_text_after != one_one_text_before
        assert two_one_text_after != two_one_text_before

    '''
    测试——你的音乐补给滚动区域——右滚动
    '''
    def test_supply_scroll_right(self, QQMusic_app):
        rec_ele = read_yaml("推荐")
        all_rec_area_ele = rec_ele["推荐整个模块"]
        all_rec_area = QQMusic_app.win.child_window(auto_id=all_rec_area_ele["auto_id"],
                                                    control_type=all_rec_area_ele["control_type"])
        # 找推荐整个模块的中间坐标
        point = all_rec_area.rectangle().mid_point()
        # 在推荐模块鼠标下拉，展示完整的为你推荐区域
        mouse.scroll(coords=(point.x, point.y), wheel_dist=-500)
        # 点击右滚动按钮
        scroll_left_ele = rec_ele["音乐补给右滚动"]
        one_one_ele = rec_ele["音乐补给第一排第一项文本"]
        two_one_ele = rec_ele["音乐补给第二排第一项文本"]

        one_one_text_before = QQMusic_app.win.child_window(auto_id=one_one_ele["auto_id"],
                                                           control_type=one_one_ele["control_type"],
                                                           found_index=0).window_text()
        two_one_text_before = QQMusic_app.win.child_window(auto_id=two_one_ele["auto_id"],
                                                           control_type=two_one_ele["control_type"],
                                                           found_index=0).window_text()

        scroll_right_btn = QQMusic_app.win.child_window(auto_id=scroll_left_ele["auto_id"],
                                                       control_type=scroll_left_ele["control_type"])
        scroll_right_btn.click_input()
        # 左滚动结果的校验--项目名称是否变化
        one_one_text_after = QQMusic_app.win.child_window(auto_id=one_one_ele["auto_id"],
                                                          control_type=one_one_ele["control_type"],
                                                          found_index=0).window_text()
        two_one_text_after = QQMusic_app.win.child_window(auto_id=two_one_ele["auto_id"],
                                                          control_type=two_one_ele["control_type"],
                                                          found_index=0).window_text()
        assert one_one_text_after != one_one_text_before
        assert two_one_text_after != two_one_text_before
