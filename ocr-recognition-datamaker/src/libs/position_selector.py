# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import os, sys, random, math

class PositionSelector(object):
    """docstring for PositionSelector"""
    def __init__(self):
        super(PositionSelector, self).__init__()

    def get_real_size(self, text, font_path, font_size):
        img = Image.new("RGBA", (1,1))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        # print type(text), font
        w, h = draw.textsize(text, font=font)
        return w, h

    def get_text_img(self, text, font_path, font_size, font_color):
        img_t = Image.new("RGBA", (1,1))
        draw_t = ImageDraw.Draw(img_t)
        font = ImageFont.truetype(font_path, font_size)
        w, h = draw_t.text_size(text, font=font)
        # font = ImageFont.truetype(font_path, font_size)
        # img = Image.new("RGBA", text_size, (0,0,0,0))
        # draw = ImageDraw.Draw(img)
        # draw.text((0,0), text, font=font, fill=font_color)
        # return img

    def guess_size(self, text, font_size):
        n = len(text)
        return n*font_size, font_size

    def cut_text(self, text, font_size, w_limit):
        m = int(w_limit/font_size)
        n = len(text)
        if m >= n:
            return text
        else:
            p = random.randint(0, n - m)
            # print w_limit, m,n ,text[p:p+m]
            return text[p:p+m]


    def process(self, text_list, bg_img, font_path, font_size, font_color):
        W,H = bg_img.size
        target_text = text_list[0]
        g_w, g_h = self.guess_size(target_text, font_size)
        if g_w > W or g_h > H:
            return None

        r_w, r_h = self.get_real_size(target_text, font_path, font_size)



        is_out_of_rect = False
        text_size_list = []
        # print rect, font_size
        for i, text in enumerate(text_list):
            text_list[i] = self.cut_text(text, font_size, (rect[2] - rect[0]))
            t_w, t_h = self.get_real_size(text_list[i], font_path, font_size)
            text_size_list.append((t_w, t_h))

        total_height = 0
        w, h = rect[2] - rect[0], rect[3] - rect[1]
        for text_size in text_size_list:
            if text_size[0] > w:
                is_out_of_rect = True
            total_height += text_size[1]
        if total_height > h:
            is_out_of_rect = True
        if is_out_of_rect:
            return None

        result = []
        n = len(text_list)
        line_height = h*1.0/n
        if random.random() < 0.5:
            line_height = font_size
        # print line_height, n, rect
        for i in range(n):
            x1 = 0
            x2 = max(x1, w - text_size_list[i][0])
            y1 = int(line_height*i)
            y2 = max(y1, int(line_height*(i+1)) - text_size_list[i][1])
            # print 'y1: {}, y2 : {}'.format(y1, y2)
            pos_x = rect[0] +  random.randint(x1, x2)
            pos_y = rect[1] +  random.randint(y1, y2)
            result.append({'pos_x': pos_x, 'pos_y':pos_y, 'w': text_size_list[i][0], 'h': text_size_list[i][1]})
        return result
