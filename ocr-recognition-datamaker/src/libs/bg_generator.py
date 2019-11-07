# coding:utf-8

import os, sys, random, math
import yaml
from PIL import Image, ImageDraw

class BgGenerator(object):
    """docstring for BgGenerator"""
    def __init__(self, background_dir, config_path):
        super(BgGenerator, self).__init__()
        self.config = self.load_config(config_path)
        self.img_path_list = self.load_backgrounds(background_dir)
        self.now_img_path_id = 0
        self.max_img_cache = 320
        self.bg_list = []


    def load_config(self, config_path):
        result = None
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    def load_backgrounds(self, background_dir):
        img_path_list = []
        file_list = os.listdir(background_dir)
        for file_name in file_list:
            if file_name[-3:] == 'jpg':
                # img = Image.open(os.path.join(background_dir, file_name))
                # img_list.append(img)
                img_path_list.append(os.path.join(background_dir, file_name))
        return img_path_list

    def random_bg_size(self, max_w, max_h):
        w = self.config['min_bg_width']
        h = self.config['min_bg_height']
        if self.config['min_bg_width'] < min(max_w, self.config['max_bg_width']):
            w = random.randint(self.config['min_bg_width'], min(max_w, self.config['max_bg_width']))
        if self.config['min_bg_height'] < min(max_h, self.config['max_bg_height']):
            h = random.randint(self.config['min_bg_height'], min(max_h, self.config['max_bg_height']))
        return w, h

    def get_bg_img(self):
        n = len(self.bg_list)
        m = len(self.img_path_list)
        res_img = None
        if self.now_img_path_id < n:
            res_img = self.bg_list[self.now_img_path_id]
        else:
            img_path = self.img_path_list[self.now_img_path_id]
            res_img = Image.open(img_path)
            rW,rH = res_img.size
            print('background image width:{} and height:{}'.format(rW,rH))
            if n < self.max_img_cache:
                self.bg_list.append(res_img)
        self.now_img_path_id = (self.now_img_path_id + 1) % m
        return res_img

    def get_background_img(self):
        target_img = self.get_bg_img()
        W,H = target_img.size
        w, h = self.random_bg_size(W, H)
        min_x = 0
        max_x = W - w
        min_y = 0
        max_y = H - h
        x1 = random.randint(min_x, max_x)
        y1 = random.randint(min_y, max_y)
        return target_img.crop((x1, y1, x1 + w, y1 + h))

