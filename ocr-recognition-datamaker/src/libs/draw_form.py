# coding:utf-8

from PIL import Image, ImageDraw
import os, sys, random, math

class DrawForm(object):
    """docstring for DrawForm"""
    def __init__(self, min_width, min_height, max_width_nums=4, max_height_nums=4, real_draw_line=True):
        super(DrawForm, self).__init__()
        self.min_width = min_width
        self.min_height = min_height
        self.max_width_nums = max_width_nums
        self.max_height_nums = max_height_nums
        self.real_draw_line = real_draw_line
        self.defalut_color = self.random_line_color()

    def random_line_color(self):
        mean_value = random.randint(0, 128)
        c_list = []
        for i in range(3):
            v = random.randint(mean_value - 10, mean_value + 10)
            v = min(255, max(v, 0))
            c_list.append(v)
        return tuple(c_list)

    def draw_line(self, img, start_pos, end_pos, fill=(0, 0, 0), width=2):
        if self.real_draw_line:
            draw = ImageDraw.Draw(img)
            draw.line(start_pos + end_pos, fill=self.defalut_color, width=width)

    def draw_rect(self, img, start_pos, end_pos, outline=(0,0,0), width=2):
        if self.real_draw_line:
            draw = ImageDraw.Draw(img)
            draw.rectangle(start_pos + end_pos, fill=None, width=width, outline=self.defalut_color)

    def get_area_size(self, area):
        return area[2] - area[0], area[3] - area[1]

    def draw_form(self, img, area, rect_list):
        w, h = self.get_area_size(area)
        if h < self.min_height*2 or w < self.min_width:
            if w >= self.min_height and h >= self.min_height:
                rect_list.append(area)
            return
        is_can_stop = h < self.min_height*self.max_height_nums and w < self.min_width*self.max_width_nums
        if is_can_stop and random.random() < 0.5:
            if w >= self.min_height and h >= self.min_height:
                rect_list.append(area)
            return

        r_value = random.random()
        if r_value < 0.5:
            h_nums = random.randint(1, min(self.max_height_nums, int(h / self.min_height)))
            self.draw_line(img, (area[0], area[1] + h_nums*self.min_height), (area[2], area[1] + h_nums*self.min_height) )
            self.draw_form(img, [area[0], area[1], area[2], area[1] + h_nums*self.min_height], rect_list)
            self.draw_form(img, [area[0], area[1] + h_nums*self.min_height, area[2], area[3]], rect_list)
        else:
            w_nums = random.randint(1, min(3, int(w/self.min_width)))
            self.draw_line(img, (area[0] + w_nums*self.min_width, area[1]), (area[0] + w_nums*self.min_width, area[3]))
            self.draw_form(img, [area[0], area[1], area[0] + w_nums*self.min_width, area[3]], rect_list)
            self.draw_form(img, [area[0] + w_nums*self.min_width, area[1], area[2], area[3]], rect_list)
        