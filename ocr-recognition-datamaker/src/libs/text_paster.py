# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import os, sys, random, math

class TextPaster(object):
    """docstring for TextPaster"""
    def __init__(self):
        super(TextPaster, self).__init__()


    def generate_text_img(self, text, text_size,font_path, font_size, font_color):
        font = ImageFont.truetype(font_path, font_size)
        img = Image.new("RGBA", text_size, (0,0,0,0))
        draw = ImageDraw.Draw(img)
        draw.text((0,0), text, font=font, fill=font_color)
        return img

    def padding_label(self, x, y, w, h, max_w, max_h):
        x1, x2 = int(x - h/4), int(x + w + h/4)
        y1, y2 = y - 2, y + h + 2
        res = [x1, y1, x2, y2]
        for i in range(4):
            if i & 1 == 0:
                res[i] = min(max_w, max(0, res[i]))
            else:
                res[i] = min(max_h, max(0, res[i]))
        return res


    def paste_text_to_img(self, img, text_list, positions, font_path, font_size, font_color=(0,0,0)):
        label_list = []

        img_w, img_h = img.size
        for i, text in enumerate(text_list):
            x, y, w, h = positions[i]['pos_x'], positions[i]['pos_y'], positions[i]['w'], positions[i]['h']
            word_img = self.generate_text_img(text, (positions[i]['w'], positions[i]['h']), font_path, font_size, font_color)

            img.paste(word_img, (positions[i]['pos_x'], positions[i]['pos_y']), mask=word_img)
            res_pos = self.padding_label(x, y, w, h, img_w, img_h)
            res_pos.append(text)
            label_list.append(res_pos)
        return label_list


